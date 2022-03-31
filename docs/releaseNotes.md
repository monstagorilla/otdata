# Release Notes

## Version 2.0.0
A complete list of changes can be found in the [git history]

### Major Changes
- Improve tour management to handle logistics processes with complex tasks, multiple drives and detailed information about different items in shipments
- Introduce unified REST structure
- Introduce webhooks and subscriptions for asynchronous server-to-client communication 
- Introduce events to transmit status changes 
- Add new endpoints for the management of vehicles, drivers, devices, customers, shipments and tacho files
- Introduce endpoint for retrieving ETAs
- Introduce channel-based messaging
- Improve endpoint `/live-data` and add response modification
- Introducing ETag header for caching and optimistic concurrency control 
- Using URI instead of IDs
- Add license 
- Update to Open API Specification 3.0.3

### Minor Changes
- Introduce media type `application/problem+json` for detailed error responses 
- Introduce cursor-based pagination for retrieving lists from collections
- Add [license](https://gitlab.com/opentelematics/otdata/-/blob/master/LICENSE)
- Using references instead of always transmitting complete data sets
- Unify naming 

## Version 1.1.0 
A complete list of changes can be found in the [git history](https://gitlab.com/opentelematics/otdata/-/tree/1.1.0).

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
