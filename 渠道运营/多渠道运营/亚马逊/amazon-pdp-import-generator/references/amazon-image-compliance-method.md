# Amazon PDP 图片合规检查方法

## 当前基线与时效

本文件记录 2026-07-15 可见的 Amazon 官方公开基线，执行时仍须按目标站点、类目和 Seller Central 当前要求刷新：

- 每个商品至少一张图片；Amazon 建议准备多张图片。
- Amazon 官方公开说明列出最长边 500 至 10,000 像素；大于 1,000 像素更利于启用缩放。
- 公开说明接受 JPEG、TIFF、PNG 和非动画 GIF；主图或特定类目可能有更严格格式要求，应以当前站点规则为准。
- 主图通常要求实际在售商品、纯白背景 `RGB 255/255/255`、主体占画面至少 85%，且不含额外文字、图形、水印或未随商品出售的道具/配件。
- Amazon 没有对所有商品统一规定固定长宽比。必须记录实际比例并预览桌面与移动裁切，不得把经验比例冒充硬性规则。

官方参考：

- [Amazon product listings](https://sell.amazon.com/blog/amazon-product-listings)
- [Amazon product photo requirements](https://sell.amazon.com/blog/product-photos)
- [Seller Central product image requirements update](https://sellercentral.amazon.com/seller-forums/discussions/t/4b3c4c39-6f8c-4312-aa0e-99982eb8f5e1)

## 两层检查

### 技术层，可自动化

- 文件能否读取、真实格式、扩展名、动画状态和损坏情况。
- 宽、高、最长边、文件字节、长宽比、缩放资格。
- 文件名与 SKU/图片角色映射、重复内容、缺主图和顺序。

### 视觉与权利层，必须人工或视觉模型后再人工复核

- 主图背景、主体占比、清晰度、边缘、阴影和实际商品准确性。
- 文字、Logo、水印、徽章、比较、促销、评价、认证和效果声明。
- 道具或配件是否包含，颜色/尺寸/数量/变体是否与在售 SKU 一致。
- 模特、肖像、字体、素材、商标和第三方作品的授权范围。
- 类目特殊要求、儿童/成人内容、安全、医疗或受限商品表达。

## 状态

- `PASS_TECHNICAL`：仅表示技术检查通过，仍须视觉和权利复核。
- `WARNING`：可读取但存在缩放、比例、格式偏好或人工检查项。
- `BLOCK`：违反已核实硬规则、文件损坏或与 SKU 身份冲突。
- `REVIEW_REQUIRED`：当前规则不可访问、类目特殊规则未知或视觉/权利无法确认。
