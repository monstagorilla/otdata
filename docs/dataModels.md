# Data Models
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

## Types
Overview of the data types used in the respective context.  


| Unit                | Data type        | Exceptions         |
|---------------------|------------------|--------------------|
| kilometer           | `float`          | mileage: `int32`   |
| meter               | `int32`          |                    |
| centimeter          | `number`         |                    |
| km/h                | `float`          |                    |
| rpm                 | `int32`          |                    |
| liter, l/h          | `float`          | total fuel: `int32`| 
| %                   | `int32`          |                    |
| temperature in °C   | `float`          |                    |
| pressure in kPa     | `ìnt32`          |                    |
| kg                  | `int32`          |                    |
| voltage in V        | `float`          |                    |
| seconds             | `int32`          |                    |
| longitude, latitude in meter| `double` |                    |


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
| `refdid`   | Reference Device ID     |
| `dataid`   | Data ID      |

## Date and time indications  
Unless otherwise stated, we use the ISO 8601 specification for all types of times.  
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
    "example": "2017-07-21"
}```

