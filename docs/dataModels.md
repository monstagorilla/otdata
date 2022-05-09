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
        }
    }
}
```

## Date and time indications  
Unless otherwise stated, we use the [ISO 8601](https://tools.ietf.org/html/rfc3339#section-5.6) specification for all types of times.   
   
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
}
```

