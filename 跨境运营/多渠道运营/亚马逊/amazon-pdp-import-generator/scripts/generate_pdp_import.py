#!/usr/bin/env python3
import argparse
import csv
import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROLE_PRIORITY = {
    "main": 0,
    "front": 1,
    "side": 2,
    "back": 3,
    "detail": 4,
    "lifestyle": 5,
    "package": 6,
    "unknown": 99,
}

PARSE_LOG_COLUMNS = [
    "file_name",
    "tokens",
    "base_tokens",
    "sku",
    "parent_sku",
    "product_type",
    "color_name",
    "role",
    "sequence",
    "parse_confidence",
]


def load_config(config_path: Path) -> dict:
    with config_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def split_tokens(stem: str) -> list[str]:
    return [token for token in re.split(r"[-_\s]+", stem.strip()) if token]


def normalize_token(token: str) -> str:
    return token.strip().lower()


def is_sequence_token(token: str) -> bool:
    return bool(re.fullmatch(r"(?:img|image)?0*\d+", token))


def peel_trailing_markers(tokens: list[str], role_aliases: dict[str, str]) -> tuple[list[str], str, str]:
    base_tokens = tokens[:]
    role = "unknown"
    sequence = ""

    while base_tokens:
        last = normalize_token(base_tokens[-1])
        if last in role_aliases:
            if role == "unknown":
                role = role_aliases[last]
            base_tokens.pop()
            continue
        if is_sequence_token(last):
            if not sequence:
                sequence = re.sub(r"^(?:img|image)?0*", "", last) or "0"
            base_tokens.pop()
            continue
        break

    return base_tokens or tokens[:], role, sequence


def infer_segments(base_tokens: list[str], known_colors: set[str], stop_tokens: set[str]) -> dict:
    normalized = [normalize_token(token) for token in base_tokens]
    id_index = next((idx for idx, token in enumerate(normalized) if any(char.isdigit() for char in token)), None)

    if id_index is None:
        product_type_tokens = base_tokens[:1] or [base_tokens[0]]
        core_id = base_tokens[1] if len(base_tokens) > 1 else base_tokens[0]
        attribute_tokens = base_tokens[2:] if len(base_tokens) > 2 else []
        confidence = "medium"
    else:
        product_type_tokens = base_tokens[:id_index] or [base_tokens[0]]
        core_id = base_tokens[id_index]
        attribute_tokens = base_tokens[id_index + 1 :]
        confidence = "high" if attribute_tokens else "medium"

    color = ""
    for token in attribute_tokens:
        normalized_token = normalize_token(token)
        if normalized_token in known_colors:
            color = normalized_token
            break

    if not color:
        for token in attribute_tokens:
            normalized_token = normalize_token(token)
            if normalized_token not in stop_tokens and not is_sequence_token(normalized_token):
                color = normalized_token
                break

    product_type = " ".join(product_type_tokens).strip()
    parent_sku = "-".join(product_type_tokens + [core_id]).strip("-")
    sku = "-".join(base_tokens)

    title_parts = [to_title(product_type)]
    if color:
        title_parts.append(to_title(color))

    return {
        "sku": sku,
        "parent_sku": parent_sku,
        "product_type": product_type,
        "color_name": color,
        "item_name_seed": " ".join(part for part in title_parts if part).strip(),
        "parse_confidence": confidence,
    }


def to_title(text: str) -> str:
    return " ".join(word.capitalize() for word in text.replace("-", " ").split())


def choose_main_image(images: list[dict]) -> tuple[dict, list[dict]]:
    sorted_images = sorted(
        images,
        key=lambda image: (
            ROLE_PRIORITY.get(image["role"], ROLE_PRIORITY["unknown"]),
            int(image["sequence"]) if image["sequence"].isdigit() else 999,
            image["name"].lower(),
        ),
    )
    return sorted_images[0], sorted_images[1:]


def scan_images(input_dir: Path, config: dict) -> tuple[list[dict], list[dict]]:
    image_extensions = {extension.lower() for extension in config["image_extensions"]}
    role_aliases = {key.lower(): value for key, value in config["role_aliases"].items()}
    known_colors = {color.lower() for color in config["known_colors"]}
    stop_tokens = {token.lower() for token in config["stop_tokens"]}

    grouped_images: dict[str, list[dict]] = defaultdict(list)
    parse_log: list[dict] = []

    files = sorted(
        file for file in input_dir.rglob("*") if file.is_file() and file.suffix.lower() in image_extensions
    )
    if not files:
        raise FileNotFoundError(f"在 {input_dir} 中未找到可识别图片文件")

    for file in files:
        tokens = split_tokens(file.stem)
        if not tokens:
            continue

        base_tokens, role, sequence = peel_trailing_markers(tokens, role_aliases)
        inferred = infer_segments(base_tokens, known_colors, stop_tokens)
        image_item = {
            "path": str(file),
            "name": file.name,
            "role": role,
            "sequence": sequence,
        }
        grouped_images[inferred["sku"]].append(image_item)

        parse_log.append(
            {
                "file_name": file.name,
                "tokens": "|".join(tokens),
                "base_tokens": "|".join(base_tokens),
                "sku": inferred["sku"],
                "parent_sku": inferred["parent_sku"],
                "product_type": inferred["product_type"],
                "color_name": inferred["color_name"],
                "role": role,
                "sequence": sequence,
                "parse_confidence": inferred["parse_confidence"],
            }
        )

    rows = []
    for sku, images in sorted(grouped_images.items()):
        sample_tokens = split_tokens(Path(images[0]["name"]).stem)
        base_tokens, _, _ = peel_trailing_markers(sample_tokens, role_aliases)
        inferred = infer_segments(base_tokens, known_colors, stop_tokens)
        main_image, other_images = choose_main_image(images)

        rows.append(
            {
                "sku": inferred["sku"],
                "parent_sku": inferred["parent_sku"],
                "product_type": to_title(inferred["product_type"]),
                "color_name": to_title(inferred["color_name"]),
                "item_name": inferred["item_name_seed"],
                "brand_name": "",
                "marketplace": "",
                "category": "",
                "variation_theme": "Color",
                "main_image_file": main_image["name"],
                "other_image_files": ", ".join(image["name"] for image in other_images),
                "main_image_url": "",
                "other_image_urls": "",
                "bullet_point_1": "",
                "bullet_point_2": "",
                "bullet_point_3": "",
                "bullet_point_4": "",
                "bullet_point_5": "",
                "product_description": "",
                "search_terms": "",
                "parse_confidence": inferred["parse_confidence"],
                "source_files": ", ".join(image["name"] for image in sorted(images, key=lambda item: item["name"].lower())),
            }
        )

    return rows, parse_log


def apply_defaults(rows: list[dict], args: argparse.Namespace) -> list[dict]:
    for row in rows:
        if args.brand:
            row["brand_name"] = args.brand
            row["item_name"] = " ".join(part for part in [args.brand, row["item_name"]] if part).strip()
        row["marketplace"] = args.marketplace
        row["category"] = args.category
        row["variation_theme"] = args.variation_theme
    return rows


def write_csv(rows: list[dict], columns: list[str], output_path: Path) -> None:
    with output_path.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


def column_name(index: int) -> str:
    result = ""
    while index > 0:
        index, remainder = divmod(index - 1, 26)
        result = chr(65 + remainder) + result
    return result


def xml_text(value: str) -> str:
    safe = escape(value or "")
    if safe.startswith(" ") or safe.endswith(" "):
        return f'<t xml:space="preserve">{safe}</t>'
    return f"<t>{safe}</t>"


def build_sheet_xml(rows: list[list[str]]) -> str:
    lines = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">',
        "<sheetData>",
    ]

    for row_index, row in enumerate(rows, start=1):
        lines.append(f'<row r="{row_index}">')
        for column_index, cell_value in enumerate(row, start=1):
            cell_ref = f"{column_name(column_index)}{row_index}"
            lines.append(
                f'<c r="{cell_ref}" t="inlineStr"><is>{xml_text(str(cell_value))}</is></c>'
            )
        lines.append("</row>")

    lines.extend(["</sheetData>", "</worksheet>"])
    return "".join(lines)


def write_xlsx(sheet_map: dict[str, list[list[str]]], output_path: Path) -> None:
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    workbook_sheets = []
    workbook_rels = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">',
    ]
    content_types = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">',
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>',
        '<Default Extension="xml" ContentType="application/xml"/>',
        '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>',
        '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>',
        '<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>',
    ]

    root_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>"""

    for index, (sheet_name, sheet_rows) in enumerate(sheet_map.items(), start=1):
        workbook_sheets.append(
            f'<sheet name="{escape(sheet_name)}" sheetId="{index}" r:id="rId{index}"/>'
        )
        workbook_rels.append(
            f'<Relationship Id="rId{index}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{index}.xml"/>'
        )
        content_types.append(
            f'<Override PartName="/xl/worksheets/sheet{index}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
        )

    workbook_rels.append("</Relationships>")
    content_types.append("</Types>")

    workbook_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        "<sheets>"
        + "".join(workbook_sheets)
        + "</sheets></workbook>"
    )

    core_xml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
 xmlns:dc="http://purl.org/dc/elements/1.1/"
 xmlns:dcterms="http://purl.org/dc/terms/"
 xmlns:dcmitype="http://purl.org/dc/dcmitype/"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:creator>SkillForge</dc:creator>
  <cp:lastModifiedBy>SkillForge</cp:lastModifiedBy>
  <dcterms:created xsi:type="dcterms:W3CDTF">{now}</dcterms:created>
  <dcterms:modified xsi:type="dcterms:W3CDTF">{now}</dcterms:modified>
</cp:coreProperties>"""

    app_xml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"
 xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>SkillForge</Application>
  <TitlesOfParts>
    <vt:vector size="{len(sheet_map)}" baseType="lpstr">
      {''.join(f'<vt:lpstr>{escape(name)}</vt:lpstr>' for name in sheet_map.keys())}
    </vt:vector>
  </TitlesOfParts>
</Properties>"""

    with ZipFile(output_path, "w", compression=ZIP_DEFLATED) as workbook:
        workbook.writestr("[Content_Types].xml", "".join(content_types))
        workbook.writestr("_rels/.rels", root_rels)
        workbook.writestr("xl/workbook.xml", workbook_xml)
        workbook.writestr("xl/_rels/workbook.xml.rels", "".join(workbook_rels))
        workbook.writestr("docProps/core.xml", core_xml)
        workbook.writestr("docProps/app.xml", app_xml)

        for index, (_, sheet_rows) in enumerate(sheet_map.items(), start=1):
            workbook.writestr(f"xl/worksheets/sheet{index}.xml", build_sheet_xml(sheet_rows))


def build_sheet_rows(columns: list[str], rows: list[dict]) -> list[list[str]]:
    table = [columns]
    for row in rows:
        table.append([row.get(column, "") for column in columns])
    return table


def build_log_rows(parse_log: list[dict]) -> list[list[str]]:
    table = [PARSE_LOG_COLUMNS]
    for row in parse_log:
        table.append([row.get(column, "") for column in PARSE_LOG_COLUMNS])
    return table


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="根据商品图片文件名生成亚马逊 PDP 导入草稿表")
    parser.add_argument("input_dir", help="存放商品图片的目录")
    parser.add_argument("--output-dir", help="输出目录，默认写入输入目录")
    parser.add_argument("--brand", default="", help="品牌名，会自动拼进 item_name")
    parser.add_argument("--marketplace", default="US", help="站点标记，默认 US")
    parser.add_argument("--category", default="", help="类目名称")
    parser.add_argument("--variation-theme", default="Color", help="变体主题，默认 Color")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    skill_root = Path(__file__).resolve().parent.parent
    config = load_config(skill_root / "assets" / "parser_config.json")

    input_dir = Path(args.input_dir).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve() if args.output_dir else input_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    rows, parse_log = scan_images(input_dir, config)
    rows = apply_defaults(rows, args)

    columns = config["output_columns"]
    csv_path = output_dir / "amazon_pdp_import_draft.csv"
    xlsx_path = output_dir / "amazon_pdp_import_draft.xlsx"
    parse_log_path = output_dir / "parse_log.csv"

    write_csv(rows, columns, csv_path)
    write_csv(parse_log, PARSE_LOG_COLUMNS, parse_log_path)
    write_xlsx(
        {
            "PDP_Draft": build_sheet_rows(columns, rows),
            "Parse_Log": build_log_rows(parse_log),
        },
        xlsx_path,
    )

    print(f"已生成：{xlsx_path}")
    print(f"已生成：{csv_path}")
    print(f"已生成：{parse_log_path}")


if __name__ == "__main__":
    main()
