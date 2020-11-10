# Request Structure 
## Parameter Structure
Each request has at least the following parameters:  
- `otid` (required): Registered OpenTelematics ID of the requester
- `version`: Version of the OpenTelematics API used, e.g.:`"1.1.0"`  
- `token`: JSON Web Token
  
For all primitive types query parameters are used. Objects and tokens are transmitted in the body.  


## Response Body
Each "200: OK" response body consists of four fields:
- `otid` (required): Registered OpenTelematics ID of the responder
- `version`: Version of the OpenTelematics API used, e.g.:`"1.1.0"`
- `message`: Further explanation
- `data`: Object that contains the actual data

## HTTP Status Codes  
Overview of the use of HTTP Status Codes. 

In the body of all error codes optional error messages and custom error codes can be returned.
  
**Successful (2xx):**  
There is always only **one** of the following status codes available for successfully responding to a request.  
  
- "200: OK": If the successful response contains data, even if it is an empty object. Example:  
`GET /otdata/gethistory`: "200" is the only successful status code. A list of data is returned in the body. If no data is available in the specified time interval, an empty list is returned.  
  
- "204: No Content": If the successful response to a request does not contain a body with data. Example:  
`POST /otmessage/message`: "204" is the only successful status code, because the response never contains data.  

**Client Error (4xx):**  
- "400: Bad Request": If there is a formally invalid use or combination of parameters or an incorrect request syntax. Example:  
`GET /otdata/gethistory`: Some possible reasons why "400" may be returned: The "from" parameter is an integer or the format does not match ISO 8601. Due to a typo, a parameter called "fron" is transferred.  
  
- "401: Unauthorized": If authentication is required and has failed or not yet been provided. Example:  
`GET /otdata/getlive`: The transmitted "token" is rejected by the server.
  
- "403: Forbidden": If valid authentication credentials were provided in the request but are not considered sufficient by the server to grant access.	Return - "404: Not Found" instead, if you do not want to expose that type of information. Example:  
`GET /otdata/getlive`: The transmitted "token" is accepted by the server but you do not have permission for the specific "did"
  
- "404: Not Found": If the server has not found anything matching the effective request URI. Example:  
`GET /otdata/getlive`: The server cannot map the transmitted "did" to a resource.
  
**Server Error (5xx):**  
-   "500: Internal Server Error": General error message for all types of server errors.
