# API Contract Checklist

## Common

- Consumer, actor, authorization, tenant boundary, correlation identifier
- Schema types, formats, required fields, omission, null, empty, default
- Stable machine error codes and safe messages
- Rate limits, timeouts, retries, observability, sensitive-data handling
- Compatibility, deprecation, examples, consumer tests

## HTTP

- Resource identity, operation semantics, status code, content type
- Filtering, sorting, pagination, maximum page size
- Idempotency key, deduplication window, optimistic concurrency
- Bulk atomicity, partial failure, conditional requests, caching

## Events

- Event identity, producer, topic, ordering scope, partition key
- Delivery guarantee, replay, duplication, poison-message handling
- Event time versus processing time, schema registry, retention
- Consumer compatibility and backfill behavior

## Breaking-change traps

- New required request field or newly non-null response field
- Narrowed type, reduced range, changed units or timezone
- Removed or renamed enum value, field, operation, or error code
- Changed default, sort, pagination, authorization, or side effect
- Previously accepted input now rejected
