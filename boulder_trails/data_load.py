# python script to parse trail data from GEOJSON file and upload Trail/TrailClosure objects to database
# Author: Harold Ainsworth
#
# JSON Object is in following format w each trail object as feature in features list
#
#{
#"type": "FeatureCollection",
#"name": "OSMP_Trails",
#"crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
#"features": [
#    {
#        "properties": {
#            "GISPROD3OSMPTrailsOSMPOBJECTID": 644,
#            "GISPROD3OSMPTrailsOSMPOWNER": "OSMP",
#            "GISPROD3OSMPTrailsOSMPBICYCLES": "No",
#            "GISPROD3OSMPTrailsOSMPTRAILTYPE": "Hiking Trail",
#            "GISPROD3OSMPTrailsOSMPSEGMENTID": "244-130-127",
#            "GISPROD3OSMPTrailsOSMPHORSES": "Yes",
#            "GISPROD3OSMPTrailsOSMPTRLID": 244,
#            "GISPROD3OSMPTrailsOSMPMILEAGE": 0.252,
#            "GISPROD3OSMPTrailsOSMPMEASUREDFEET": 1353,
#            "GISPROD3OSMPTrailsOSMPTRAILNAME": "Wood's Quarry",
#            "GISPROD3OSMPTrailsOSMPGlobalID": "{772F12D4-8A24-4580-9712-45E1042B9FA2}",
#            "GISPROD3OSMPTrailsOSMPDogs": null,
#            "GISPROD3OSMPTrailsOSMPDogRegGen": null,
#            "GISPROD3OSMPTrailsOSMPDogRegDesc": null,
#            "SHAPESTLength": 1329.3942342588316,
#            "GISPROD3OSMPTrailClosuresOBJECTID": 466,
#            "GISPROD3OSMPTrailClosuresCLOSUREDURATION": null,
#            "GISPROD3OSMPTrailClosuresWEBLINK": null,
#            "GISPROD3OSMPTrailClosuresCLOSUREAREA": null,
#            "GISPROD3OSMPTrailClosuresTRAILSTATUS": "Open",
#            "GISPROD3OSMPTrailClosuresCLOSUREREASON": null,
#            "GISPROD3OSMPTrailClosuresLOCATIONDESCRIPTION": null,
#            "GISPROD3OSMPTrailClosuresCONTACT": "https:\/\/bouldercolorado.gov\/osmp\/temporary-closures",
#            "GISPROD3OSMPTrailClosuresCOMMENTS": null,
#            "GISPROD3OSMPTrailClosuresGLOBALID": "{D82FC0E1-049B-4B72-AC38-CFF14D734E50}"
#        },
#        "geometry": { "type": "LineString", "coordinates": [
#               [ -105.288155758543667, 39.985455226662815 ],
#               [ -105.288151825979568, 39.985463430698353 ],
#               [ -105.288146546425011, 39.985472558130603 ]
#               ...
#           ]
#        }
#    },
#    ...
#]}

import sys
import os
import json

from trails.models import TrailSegment, TrailClosure, Trail
from django.contrib.gis.geos import LineString


jsonPath = '/Users/harryainsworth/Desktop/Projects/Boulder_Trails/OSMP_Trails.geojson'  # enter in your own json path
print("Attempting to load from GEOJSON file '{}'".format(jsonPath))

# check to make sure that the json file actually exists
if (not os.path.isfile(jsonPath)) :
    print('The JSON file does not exist')
    sys.exit(1)


# read trail data JSON object from file
with open(jsonPath) as file:
    trail_data = json.loads(file.read())

    # delete existing objects from database
    Trail.objects.all().delete()
    TrailSegment.objects.all().delete()
    TrailClosure.objects.all().delete()

    # iterate through each trail/feature in features list
    for feature in trail_data['features']:

        # check if Trail object already exists for trail segment, if not create new Trail
        if Trail.objects.filter(trail_id=feature['properties']['GISPROD3OSMPTrailsOSMPTRLID']).exists():
            trail = Trail.objects.get(pk=feature['properties']['GISPROD3OSMPTrailsOSMPTRLID'])
        else:
            trail = Trail(
                trail_id=feature['properties']['GISPROD3OSMPTrailsOSMPTRLID'],
                trail_name=feature['properties']['GISPROD3OSMPTrailsOSMPTRAILNAME']
            )
            trail.save()

        # check if TrailClosure object already exists for trail segment, if not create new TrailSegment
        if TrailClosure.objects.filter(object_id=feature['properties']['GISPROD3OSMPTrailsOSMPOBJECTID']).exists():
            trail_closure = Trail.objects.get(pk=feature['properties']['GISPROD3OSMPTrailClosuresOSMPOBJECTID'])
        else:
            trail_closure = TrailClosure(
                object_id=feature['properties']['GISPROD3OSMPTrailsOSMPOBJECTID'],
                closure_duration=feature['properties']['GISPROD3OSMPTrailClosuresCLOSUREDURATION'],
                closure_reason=feature['properties']['GISPROD3OSMPTrailClosuresCLOSUREREASON'],
                closure_area=feature['properties']['GISPROD3OSMPTrailClosuresCLOSUREAREA'],
                trail_status=feature['properties']['GISPROD3OSMPTrailClosuresTRAILSTATUS']
            )
            trail_closure.save()

        # create new TrailSegment object and populate datafields
        if feature['properties']['GISPROD3OSMPTrailsOSMPBICYCLES'] == 'Yes':
            bikes = True
        else: bikes = False

        if feature['properties']['GISPROD3OSMPTrailsOSMPHORSES'] == 'Yes':
            horses = True
        else: horses = False

        if feature['properties']['GISPROD3OSMPTrailsOSMPDogs'] == 'Yes':
            dogs = True
        else: dogs = False

        if feature['properties']['GISPROD3OSMPTrailsOSMPMEASUREDFEET'] == -9999:
            measured_feet = None
        else: measured_feet = feature['properties']['GISPROD3OSMPTrailsOSMPMEASUREDFEET']

        trail_geometry = LineString(feature['geometry']['coordinates'])

        trail_segment = TrailSegment(
            parent_trail=trail,
            closure_info=trail_closure,
            segment_id=feature['properties']['GISPROD3OSMPTrailsOSMPSEGMENTID'],
            owner=feature['properties']['GISPROD3OSMPTrailsOSMPOWNER'],
            bikes=bikes,
            trail_type=feature['properties']['GISPROD3OSMPTrailsOSMPTRAILTYPE'],
            horses=horses,
            mileage=feature['properties']['GISPROD3OSMPTrailsOSMPMILEAGE'],
            measured_feet=measured_feet,
            dogs=dogs,
            st_length=feature['properties']['SHAPESTLength'],
            geometry=trail_geometry
        )
        trail_segment.save()

print("success!")