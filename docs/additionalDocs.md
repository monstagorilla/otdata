# Additional Documentation
## Date and time indications  
Unless otherwise stated, we use use the ISO 8601 specification for all types of times.  
https://tools.ietf.org/html/rfc3339#section-5.6 
   
Use the OpenAPI format `“date-time”` for ISO 8601 "date-time":   
```json
"deadline": {
    "type": "string",
    "format": "date-time",
    "example": "2017-07-22T17:32:28Z"
}
```
Use the OpenAPI format `“date”` for ISO 8601 "full-date":
```json
"valid_from": {
    "type": "string",
    "format": "date",
    "example": "01.12.2006"
}
```
## Basic schema for vehicle data in API responses  
Data that can be not available or faulty are returned in a tuple-like structure with a `"status"` property and a `"value"` property. The `"status"` property has three possible values: `“ok”` (data is available), `“error”` (an error occurred) and `“n/a”` (data is not available e.g. vehicle is turned off). The `"value"` property holds the actual data.
You can verify the correctness of the data with the `“status”` and if it is `“ok”`, access the `“value”`.  
```json
"caninstant": {
    "type": "object",
    "properties":
        "speed": {
            "type": "object",
            "required": ["status"],
            "properties": {
                "status": {
                    "type": "string",
                    "enum": ["ok", "error", "n/a"],
                    "description": "Indicates availability of data"
                    },
                "value":{
                    "type": "number",
                    "format": "float",
                    "default": "0.0",
                    "description": "Speed in km/h"   
                }
            }
        },
    . . .
    }
},
```
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

## IDs
Overview of the different types of IDs. 
  
All IDs are `strings`. With the exception of `otid`, which is assigned by OpenTelematics, all IDs can have their own structure and are defined by the software company or the customer.

|ID          | Description |
|------------|-------------|
| `cid`      | Customer ID   |
| `gid`      | Vehicle Group ID: Identifies a vehicle group that represents a set of Device IDs.     |
| `otid`     | OpenTelematics ID: Every member of OpenTelematics e.V. has a registered ID. Both the requester and the responder transfer their `otid` so that each participant can assign it to the respective member. You can request the IDs of all members with `GET /otmember/getmember`.|
| `did`      | Device ID: Identifies a specific device or vehicle.     |
| `refid`    | Reference ID     |
| `refdid` | Reference Device ID     |
| `dataid`      | Data ID      |