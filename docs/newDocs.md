# new
## ETag Header
## Naming Conventions
| Content Type        | Naming Convention| Example|
|---------------------|------------------|------------------|
| OAS abstractions, fields <br/>in data structures, query <br/>and path parameters| snake_case | `good_example` | 
| Custom header               | Capitalized and Kebab-Case <br/>as is the case with almost <br/>all HTTP standard headers | `API-Version` |
| Endpoints          | lowercase and kebab-case | `/live-data` |

## URI in addition to IDs
Much more understandable documentation without the need for external information, because path templating is not mandatory. You can directly make a GET request on a returned URI instead of combining the returned IDs with a specified path template to a valid URI. In addition, for example, customer data can be managed on another server and the exact endpoint can be explicitly specified with a URL (subtype of URI), which is not possible via IDs and local path templating. 

## Webhook

## Cursor-based Pagination
We use cursor-based pagination (also known as keyset pagination) because it has some advantages over offset-based pagination. There is no page drifting when new datasets are added between two requests and it scales well with a large number of datasets respectively large offsets.  
The `limit` parameter sets the desired number of datasets to be returned in the response. With each response of the server it returns a `next_cursor` field, that should be used as `cursor` parameter in the next request. If there are no more datasets, the `next_cursor` field is empty.  

## application/problem+json MIME type
As defined in [RFC7807](https://datatracker.ietf.org/doc/html/rfc7807). It is used as media type of error responses (HTTP status codes 4xx and 5xx) to provide details about the occurred error in machine- and human-readable form.
