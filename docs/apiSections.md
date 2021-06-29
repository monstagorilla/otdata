

# API Sections

## Live Data
## Tour Management

Simplified Structure:

```mermaid
%%{init: {'theme': 'base','themeVariables': { 'fontFamily': 'Source Sans Pro'}}}%%
graph LR
   subgraph ExtendedOrder
   direction TB
   subgraph BasicOrder
   Tour --array--> Drive
  
   end
   Drive --array--> Shipment --array--> Item & Task
   Drive --> Address
   Drive --> TimeWindow
   end
```

## Tacho
## 