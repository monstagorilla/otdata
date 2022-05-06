# API Sections

## Live Data

You can retrieve the current data or a history of datasets within a specified time interval. The data consists of: 

- Position and movement data
- Driver and passenger information
- CAN and FMS data 
- Diagnostic trouble codes (DTC)
- Temperature data
- IO status
- Driver behaviour

## Tour Management

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'fontFamily': 'Source Sans Pro'}}}%%
graph TB
   subgraph Tour
   /tours --> /tours/1
   /tours/1 --> /tours/1/drives
   /tours/1/drives --> /tours/1/drives/1
   /tours/1/drives --> /tours/1/drives/2

   /tours/1/drives/1 --> /tours/1/drives/1/tasks
   /tours/1/drives/1/tasks --> /tours/1/drives/1/tasks/delivery
   /tours/1/drives/1/tasks --> /tours/1/drives/1/tasks/pickup

   /tours/1/drives/2 --> /tours/1/drives/2/tasks
   /tours/1/drives/2/tasks --> /tours/1/drives/2/tasks/delivery
   end
   subgraph Shipments
   /shipments --> /shipments/1
   /shipments --> /shipments/2

   /shipments/1 -.- /tours/1/drives/1/tasks/delivery
   /shipments/2 -.- /tours/1/drives/1/tasks/pickup
   /shipments/2 -.- /tours/1/drives/2/tasks/delivery
   end
```

A `tour` consists of a number of `drives`. 

### Drive

A drive has a target address and time windows for starting and arrival times. The `ExtendedOrder` structure has additionally a list of shipments, that need to be processed at the certain target address and information about dangerous goods that are loaded during the drive. The start of a tour is also a `drive`.

### Shipments

A shipment has a fixed list of items and a list of tasks to be completed at the end of the drive. 

### Items
 An item has an `id` and a `parentID`, so there is the possibility to represents a tree structure (e.g. a pallet of boxes with hard drives inside that all have their own ids). It also has detailed information about dimensions, codes (e.g. barcodes) and dangerous goods.

### Tasks

A task has a custom defined `tasktype` (e.g. "delivery"), a further `address` if it for example must be carried out at special coordinates on a factory site and a `timewindow`. There is also a list of generic key-value pairs so that it is also possible to define complex custom tasks.

### Examples for some typical requests
#### Create an entire tour with drives, tasks and linked shipments:  
- IDs and URIs assigned by server:  
`POST /shipments?create_multiple=true` or several `POST /shipments?create_multiple=false` (Create shipments associated with the new tour if they have not yet been created)  
`POST /tours?create_subresources=true` (Create the entire tour)  
- IDs and URIs assigned by client:  
`PUT /tours?create_subresources=true` (Create the entire tour and linked shipments)

Notice: When a request is used to create multiple resources, it is important to define a behavior for partial failure of the combined requests.

#### Find all tasks linked to a shipment and get events linked to the logistic process of the shipment
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
### Events and ETA

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'fontFamily': 'Source Sans Pro'}}}%%

sequenceDiagram
   participant Client
   participant Server
   participant Callback Server

   Note over Client,Server: Manage Subscriptions   
   Client->>Server: GET, POST /subscriptions
   Client->>Server: GET, PUT, DELETE /subscriptions/123
   Note over Server,Callback Server: Send Webhooks
   Server->>Callback Server: POST /webhooks/drive-event
   Server->>Callback Server: POST /webhooks/live-data
   Server->>Callback Server: POST /webhooks/eta
```

Events can be retrieved as a list (e.g. from a queue of all new and not yet downloaded events) or pushed individually. There are different kinds of events: Tour, drive and task events. Every kind of event has a `timestamp`, `coordinates` and refers to a drive and a tour. There is also an additional list of generic key-value pairs for custom content. The event types have different lists of enums for the actual event description. The task event has additional lists for status infomation of the associated shipment and its items (e.g. item condition at delivery).
You can acknowledge events if they are successfully transmitted.  

`ETA` consists of an actual `eta`for the target address and a timewindow for estimated deviations.
You can push lists of ETAs for drives or retrieve a list of ETAs for a single or all drives in a tour.  

## Tacho

You can transmit tacho data (e.g. DDD files) and retrieve information about registered drivers and vehicles.  
It is also possible to get information about activities, working periods and vehicle usage of drivers.
