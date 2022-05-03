# new
## ETag Header
## Naming Conventions
## URI vs. ID
## Webhook
## Cursor-based Pagination
We use cursor-based pagination (also known as keyset pagination) because it has some advantages over offset-based pagination. There is no page drifting when new datasets are added between two requests and it scales well with a large number of datasets respectively large offsets.  
The `limit` parameter sets the desired number of datasets to be returned in the response. With each response of the server it returns a `next_cursor` field, that should be used as `cursor` parameter in the next request. If there are no more datasets, the `next_cursor` field is empty.  

## application/problem+json MIME type
As defined in [RFC7807](https://datatracker.ietf.org/doc/html/rfc7807). It is used as media type of error responses (HTTP status codes 4xx and 5xx) to provide details about the occurred error in machine- and human-readable form.
