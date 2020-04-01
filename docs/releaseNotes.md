# Release Notes
## Version 1.1.0 
A complete list of changes can be found in the [git history](https://gitlab.com/opentelematics/otdata/-/commits/master).

### Major Changes
- Introduce strong abstractions for better reusable, more consistent and unified code
- Improve and unify descriptions
- Create website with further documentation
- Remove obligatory authentifications and add optional token parameter
- Introduce tuple-like [data structure](https://opentelematics.gitlab.io/otdata/docs/#/dataModels?id=basic-schema-for-vehicle-data-in-api-responses) for vehicle data
- Unifiy [HTTP status codes](https://opentelematics.gitlab.io/otdata/docs/#/requestStructure?id=http-status-codes)
- Unify [response bodies](https://opentelematics.gitlab.io/otdata/docs/#/requestStructure?id=response-body) 
- Unify [request parameters](https://opentelematics.gitlab.io/otdata/docs/#/requestStructure?id=parameter-structure)
- Unify use of [IDs](https://opentelematics.gitlab.io/otdata/docs/#/dataModels?id=ids)
- Replace `POST /otstate/setstatus` with `POST /otstate/setOrderStatus` and `POST /otstate/setMessageStatus`
- Replace all `header` parameters with `query` parameters
- Unify types

### Minor Changes
- Fix typos and grammar mistakes
- Use enums instead of integers associated with values 
- Abstract and unify many parameters and fields
- Introduce `gid` parameter
- Restructure Swagger UI
- Add string pattern for version number
- Unify [date and time indications](https://opentelematics.gitlab.io/otdata/docs/#/dataModels?id=date-and-time-indications)
- Change metadata
- Some minor changes and fixes