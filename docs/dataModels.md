# Data Models

## Additions
To transmit custom data without violating the specification, many data structures have an `additions` field, a list of generic key-value pairs.

## Date and time indications  
Unless otherwise stated, we use the [ISO 8601](https://tools.ietf.org/html/rfc3339#section-5.6) specification for all types of times.   
   
Use the OpenAPI format `date-time` for ISO 8601 "date-time":   
```json
"timestamp": {
    "type": "string",
    "format": "date-time",
    "example": "2017-07-22T17:32:28Z"
}
```
Use the OpenAPI format `date` for ISO 8601 "full-date":
```json
"valid_from": {
    "type": "string",
    "format": "date",
    "example": "2017-07-21"
}
```

