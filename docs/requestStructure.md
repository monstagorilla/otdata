# Request structure 
## Request parameters
Each request has at least the following header parameters:
- `OT-ID`: Registered OpenTelematics ID of the requester
- `Access-Token`: JSON Web Token
- `API-Version`: Version of the OpenTelematics API used, e.g.:`"2.0.0"`  
For all other primitive types query parameters are used. Entire objects are transmitted in the body.  
If the request returns a list of objects and therefore pagination is needed, it has also the following query parameters:  
- `cursor`: Cursor for [cursor-based pagination](generalConcepts.md#cursor-based-pagination). Use next_cursor from response body to get the next page.  
- `limit`: The limit parameter sets a maximum number of results to return per request.  

## Response headers
Each response has at least the following header parameters:
- `API-Version`: Version of the OpenTelematics API used, e.g.:`"2.0.0"`  
- `OT-ID`: Registered OpenTelematics ID of the responder  

Cacheable responses have also the following header parameters:
- `ETag`: Entity Tag as defined by [RFC2068](https://datatracker.ietf.org/doc/html/rfc2068#section-14.20)  
- `Cache-Control`: Header as defined by [RFC7234](https://datatracker.ietf.org/doc/html/rfc7234#section-5.2)  

## Response body
`200 OK` and `201 Created` responses have a response body with either a single object or a `data` property with a list of objects and a `next_cursor` for pagination.  
  
Responses with error status codes (4xx and 5xx) have a body conforming to the [application/problem+json MIME type](generalConcepts.md#applicationproblemjson-mime-type).

## HTTP status codes  
Overview of the use of HTTP status codes. The selection of status codes differs between the request types.
  
**Successful (2xx):**  
  
- `200 OK`: If the successful response contains data, even if it is an empty object. Example:  
`GET /live-data/latest`: `200` is the only successful status code. A list of data is returned in the body. If no data is available with the specified filters, an empty list is returned.  
  
- `201 Created`: If the request has succeeded and has led to the creation of a resource. The new resource may be returned in the response body. Example:  
`POST /shipments`: The created resource with the assigned ID and URI is returned in the response body and can be cached. 

- `204 No Content`: If the successful response to a request does not contain a body with data. Example:  
`POST /webhooks/tour-event`: "204" is the only successful status code, because the response never contains data.  

**Client Error (4xx):**  
- `400 Bad Request`: If there is a formally invalid use or combination of parameters or an incorrect request syntax. Example:  
`GET /live-data/latest`: Some possible reasons why "400" may be returned: The "from" parameter is an integer or the format does not match ISO 8601. Due to a typo, a parameter called "fron" is transferred.  
  
- `401 Unauthorized`: If authentication is required and has failed or not yet been provided. Example:  
`GET /otdata/getlive`: The transmitted "token" is rejected by the server.
  
- `403 Forbidden`: If valid authentication credentials were provided in the request but are not considered sufficient by the server to grant access. Return `404: Not Found` instead, if you do not want to expose that type of information. Example:  
`GET /live-data/123`: The transmitted "token" is accepted by the server but you do not have permission for the specific dataset.
  
- `404 Not Found`: If the server has not found anything matching the effective request URI. Example:  
`GET /live-data/123`: The server cannot map the transmitted URI to a resource.

- `412 Precondition Failed`: If the client has indicated preconditions in its headers which the server does not meet. Example:  
`PUT /shipments/123`: The transmitted ETag header doeas not match the latest ETag.
- `415 Unsupported Media Type`: If the media format of the requested data is not supported by the server, so the server is rejecting the request. Example:  
`POST /shipments`: The request body is not of the `application/json` MIME type.
- `428 Precondition Required`: If the origin server requires the request to be conditional. Example:  
`PUT /shipments/123`: The update is transmitted without required ETag header.  

**Server Error (5xx):**  
- `500 Internal Server Error`: General error message for all types of server errors.
- `503 Service Unavailable`: If the server is not ready to handle the request. Common causes are a server that is down for maintenance or that is overloaded.
