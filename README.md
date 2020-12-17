# Boulder Trail Running Path Generator 
Harold Ainsworth, Fall 2020


## Project Goals
- Provide a user interface allowing trail exploration
- Use custom pathfinding algorithms to generate new running/hiking loops based on user-provided starting location and desired distance


## Data 
Boulder trail data for this project was found at this [respository for OSMP data](https://data-boulder.opendata.arcgis.com/datasets/d7ad8e150c164c32ab1690658f3fa662_4). 
The data can be retrieved from this site in many formats, but this application is designed to consume GEOJSON datafiles.
See below for sample datafile:
```JSON
{
"type": "FeatureCollection",
"name": "OSMP_Trails",
"crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
"features": [
    {
        "properties": {   
            "GISPROD3OSMPTrailsOSMPOBJECTID": 644, 
            "GISPROD3OSMPTrailsOSMPOWNER": "OSMP", 
            "GISPROD3OSMPTrailsOSMPBICYCLES": "No", 
            "GISPROD3OSMPTrailsOSMPTRAILTYPE": "Hiking Trail",
            "GISPROD3OSMPTrailsOSMPSEGMENTID": "244-130-127",
            "GISPROD3OSMPTrailsOSMPHORSES": "Yes",
            "GISPROD3OSMPTrailsOSMPTRLID": 244,
            "GISPROD3OSMPTrailsOSMPMILEAGE": 0.252,
            "GISPROD3OSMPTrailsOSMPMEASUREDFEET": 1353,
            "GISPROD3OSMPTrailsOSMPTRAILNAME": "Wood's Quarry",
            "GISPROD3OSMPTrailsOSMPGlobalID": "{772F12D4-8A24-4580-9712-45E1042B9FA2}",
            "GISPROD3OSMPTrailsOSMPDogs": null,
            "GISPROD3OSMPTrailsOSMPDogRegGen": null, 
            "GISPROD3OSMPTrailsOSMPDogRegDesc": null, 
            "SHAPESTLength": 1329.3942342588316,
            "GISPROD3OSMPTrailClosuresOBJECTID": 466,
            "GISPROD3OSMPTrailClosuresCLOSUREDURATION": null,
            "GISPROD3OSMPTrailClosuresWEBLINK": null, 
            "GISPROD3OSMPTrailClosuresCLOSUREAREA": null,
            "GISPROD3OSMPTrailClosuresTRAILSTATUS": "Open",
            "GISPROD3OSMPTrailClosuresCLOSUREREASON": null,
            "GISPROD3OSMPTrailClosuresLOCATIONDESCRIPTION": null, 
            "GISPROD3OSMPTrailClosuresCONTACT": "https:\/\/bouldercolorado.gov\/osmp\/temporary-closures", 
            "GISPROD3OSMPTrailClosuresCOMMENTS": null, 
            "GISPROD3OSMPTrailClosuresGLOBALID": "{D82FC0E1-049B-4B72-AC38-CFF14D734E50}" 
        },
        "geometry": { "type": "LineString", "coordinates": [ [ -105.288155758543667, 39.985455226662815 ], [ -105.288151825979568, 39.985463430698353 ], [ -105.288146546425011, 39.985472558130603 ] ... ] }
    },
    ...  
]}

```
