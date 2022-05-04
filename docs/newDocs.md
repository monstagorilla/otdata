# new
## ETag header
## Naming conventions
| Content Type        | Naming Convention| Example|
|---------------------|------------------|------------------|
| OAS abstractions, fields <br/>in data structures, query <br/>and path parameters| snake_case | `good_example` | 
| Custom header               | Capitalized and Kebab-Case <br/>as is the case with almost <br/>all HTTP standard headers | `API-Version` |
| Endpoints          | lowercase and kebab-case | `/live-data` |

## URI in addition to IDs
The use of URIs leads to a much more understandable documentation without the need for external information, because path templating is not mandatory. You can directly make a GET request on a returned URI instead of combining the returned IDs with a specified path template to a valid URI. In addition, for example, customer data can be managed on another server and the exact endpoint can be explicitly specified with a URL (subtype of URI), which is not possible via IDs and local path templating. 

## Callbacks
### Webhooks
To push data asynchronously from the server to the client, so-called webhooks are used. They are defined as POST requests and can transmit, for example, events, ETAs or generic messages to a `callback_url`.
### Publish–subscribe pattern
The `callback_url` and which webhooks to send, can be defined out-of-band or managed with the `/subscriptions` endpoint in a typical publish-subscribe pattern. With the subscription, the client can specify the `callback_url`, an `access_token`, to use within the webhook request, the `topic` (e.g. `tour_event`) to subscribe to and its `expiration_time`. Every time something is published to a topic, the clients that are subscribd to it receive the corresponding webhook request. If a webhook request is not successful, it may be retried. In addition to the callbacks, there are endpoints that can be used to retrieve all the events of the different topics via GET request.

## Endpoint structure
The typical endpoint in the OTData API has always the same structure: 

| Request                 | Use                                                                   | Cacheable | Description                                  |
|-------------------------|-----------------------------------------------------------------------|-----------|----------------------------------------------|
| GET `/shipments`        | Search a collection with filters                                      | No        | Response can be returned in pages ((pagination)[link to pagination])            |
| POST `/shipments`       | Create a new resource                                                 | Yes       | ID, URI and links are assigned by the server |
| GET `/shipments/123`    | Retrieve a certain resource                                           | Yes       |                                              |
| PUT `/shipments/123`    | Create a new resource or replace an existing with the request payload | No        | ID, URI and links are assigned by the client |
| DELETE `/shipments/123` | Delete a certain resource                                             | No        |                                              |


## Cursor-based pagination
We use cursor-based pagination (also known as keyset pagination) because it has some advantages over offset-based pagination. There is no page drifting when new datasets are added between two requests and it scales well with a large number of datasets respectively large offsets.  
The `limit` parameter sets the desired number of datasets to be returned in the response. With each response of the server it returns a `next_cursor` field, that should be used as `cursor` parameter in the next request. If there are no more datasets, the `next_cursor` field is empty.  

## application/problem+json MIME type
As defined in [RFC7807](https://datatracker.ietf.org/doc/html/rfc7807). It is used as media type of error responses (HTTP status codes 4xx and 5xx) to provide details about the occurred error in machine- and human-readable form.
