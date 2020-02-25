# Release Notes
## Version 1.0.5 (work in progress)
### Major Changes
- Improve and unify descriptions
- Create website with additional documentation generated with docsify
- Remove obligatory authentifications
- Introduce tuple-like [data structure](https://opentelematics.gitlab.io/otdata/docs/#/additionalDocs?id=basic-schema-for-vehicle-data-in-api-responses) for vehicle data
- Abstract and unfiy [HTTP status codes](https://opentelematics.gitlab.io/otdata/docs/#/additionalDocs?id=http-status-codes)

### Minor Changes
- Fix typos and grammar mistakes
- Add string pattern for version number
- Use enums instead of integers associated with values 
- Add `format`, `minimum`, `maximum` and `default` values for many fields 
- Abstract and unify many parameters 
- Add `token`, `otid` and `version` for all requests
- Replace all `header` parameters with `query` parameters
- Change `mid` to `cid`
- Unify ID fields
- Small changes in requests
- Introduce `gid` parameter
- Fix wrong usage of float format for integers
- Restructure requests for Swagger UI
- Unify [date and time indications](https://opentelematics.gitlab.io/otdata/docs/#/additionalDocs?id=date-and-time-indications)
- Add and change some properties and parameters
- Change metadata