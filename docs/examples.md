# Examples
## Examples for some typical requests
**Get the latest location of a vehicle**
- Use the `object_uri` of the vehicle and the `fields` parameter:  
`GET /live-data/latest?object_uri=/objects/123&fields=position`

**Get the latest calculated ETA of a drive**
- Use the `drive_uri`:  
`GET /eta/latest?drive_uri=/tours/123/drives/123`  

**Get the tacho files (e.g. DDD) of a vehicle for the activities in a certain time window**
- Use the `object_uri` of the vehicle, the `from` and `to` parameters and the `used_time` parameter:  
`GET /tacho-files?object_uri=/objects/123&from=2022-05-06T10%3A33%3A00.140Z&to=2022-05-06T12%3A33%3A00.140Z?used_time=activity`

**Create an entire tour with drives, tasks and linked shipments:**  
- IDs and URIs assigned by server:  
`POST /shipments?create_multiple=true` or several `POST /shipments?create_multiple=false` (Create shipments associated with the new tour if they have not yet been created)  
`POST /tours?create_subresources=true` (Create the entire tour)  
- IDs and URIs assigned by client:  
`PUT /tours?create_subresources=true` (Create the entire tour and linked shipments)

Notice: When a request is used to create multiple resources, it is important to define a behavior for partial failure of the combined requests.

**Find all tasks linked to a shipment and get events linked to the logistic process of the shipment**  
Simply read the `linked_tasks` list with all the URIs of linked tasks. With those URIs it is then easy to retrieve more information about the logistic process of the shipment, simply use a subset of the `task_uri` e.g. `/tours/123/drives/123`:  
- Information about the planned drive:  
`GET /tours/123/drives/123`  
- Directly retrieve events regarding the drive:  
`GET /drive-events?drive_uri=/tours/123/drives/123`  
- Subscribe to the corresponding drive events:  
`POST /subscriptions`  
Request body:  
```json
{
  "timestamp": "2022-05-06T12:33:00.140Z",
  "callback_url": "https://webhooks.opentelematics.io",
  "access_token": "very_secure_token",
  "topic": "drive_event",
  "event_uri": "/drive-events?drive_uri=/tours/123/drives/123`",
  "expiration_time": "2022-05-06T12:33:00.140Z" 
}
```
- Send webhook for the subscribed events:  
`POST https://webhooks.opentelematics.io/drive-event`  
Request body:  
```json
{
  "id": "123",
  "uri": "/drive-events/123",
  "timestamp": "2022-05-06T12:47:26.807Z",
  "drive_uri": "/tours/123/drives/123",
  "coordinates": {
    "latitude": 0,
    "longitude": 0
  },
  "event": "started"
}
```

**Get all shipments that corresponds to a tour**  
- Instead of searching the entire tour for shipment links, it is possible to search the `/shipments` endpoint:  
`GET /shipments?tour_uri=/tours/123`
