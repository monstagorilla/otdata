# Release Notes

## Version 2.0.0
A complete list of changes can be found in the [git history](https://gitlab.com/opentelematics/otdata/-/commits/2.0.0)

### Major Changes
- Improve [tour management](apiSections.md#Tour-Management) to handle logistics processes with complex tasks, multiple drives and detailed information about different items in shipments
- Introduce unified REST [structure](generalConcepts.md#Endpoint-structure)
- Introduce [webhooks and subscriptions](generalConcepts.md#Callbacks) for asynchronous server-to-client communication 
- Introduce [events](apiSections.md#Events) to transmit status changes 
- Add new endpoints for the management of objects, drivers, customers, shipments and tacho files
- Introduce endpoint for retrieving [ETAs](apiSections.md#ETA)
- Introduce channel-based messaging
- Improve endpoint [`/live-data`](apiSections.md#live-data) and add response modification
- Introduce full support for FMS Truck and Bus Specification
- Introducing [ETag](generalConcepts.md#ETag-header) header for caching and optimistic concurrency control 
- Update to Open API Specification 3.0.3 and restructure most abstractions
### Minor Changes
- Introduce media type [`application/problem+json`](generalConcepts.md#applicationproblemjson-mime-type) for detailed error responses 
- Introduce [cursor-based pagination](generalConcepts.md#Cursor-based-pagination) for retrieving lists from collections
- Using [URI instead of IDs](generalConcepts.md#uri-in-addition-to-ids)
- Add [license](https://gitlab.com/opentelematics/otdata/-/blob/master/LICENSE)
- Using references instead of always transmitting complete data sets
- Unify [naming](generalConcepts.md#Naming-conventions) 
- Introduce [additions](dataModels.md#additions) for transmission of custom data without violating the specification.
- A lot of minor changes and fixes

## Version 1.1.0 
A complete list of changes can be found in the [git history](https://gitlab.com/opentelematics/otdata/-/commits/1.1.0).

### Major Changes
- Introduce strong abstractions for better reusable, more consistent and unified code
- Improve and unify descriptions
- Create website with further documentation
- Remove obligatory authentifications and add optional token parameter
- Introduce tuple-like data structure for vehicle data
- Unifiy HTTP status codes
- Unify response bodies
- Unify request parameters
- Unify use of IDs
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
- Unify date and time indications
- Change metadata
- Some minor changes and fixes
