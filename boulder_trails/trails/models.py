from django.contrib.gis.db import models


class TrailClosure(models.Model):
    # trail closure model based on data retrieved from OSMP trail dataset for the City of Boulder
    # https://data-boulder.opendata.arcgis.com/datasets/d7ad8e150c164c32ab1690658f3fa662_4
    # see OSMP_Trails.geojson for datafield specifics

    object_id = models.IntegerField(primary_key=True)  # id for the trail segment closure object
    closure_duration = models.CharField(max_length=100, null=True)  # msg indicating how long trail will be closed for
    closure_reason = models.CharField(max_length=100, null=True)  # reason trail is closed, if applicable
    closure_area = models.CharField(max_length=100, null=True)  # the name of area represented by TrailClosure object
    trail_status = models.CharField(max_length=50)  # indicates trail closure/condition status


class Trail(models.Model):
    # trail segment model based on data retrieved from OSMP trail dataset for the City of Boulder
    # https://data-boulder.opendata.arcgis.com/datasets/d7ad8e150c164c32ab1690658f3fa662_4
    # see OSMP_Trails.geojson for datafield specifics

    trail_id = models.IntegerField(primary_key=True)  # id value of the trail
    trail_name = models.CharField(max_length=100)  # name of the trail

    def __str__(self):
        return self.trail_name


class TrailSegment(models.Model):
    # trail segment model based on data retrieved from OSMP trail dataset for the City of Boulder
    # https://data-boulder.opendata.arcgis.com/datasets/d7ad8e150c164c32ab1690658f3fa662_4
    # see OSMP_Trails.geojson for datafield specifics

    # foreign key fields
    parent_trail = models.ForeignKey(Trail, on_delete=models.CASCADE)  # parent trail that trail segment is a part of
    closure_info = models.ForeignKey(TrailClosure, on_delete=models.SET_NULL, null=True)  # points to closure object

    # data fields
    segment_id = models.CharField(max_length=50, primary_key=True)  # unique trail segment ID used as primary key
    owner = models.CharField(max_length=50, null=True)  # owner of trail segment
    bikes = models.BooleanField()  # indicates if bikes are allowed on trail segment
    trail_type = models.CharField(max_length=50, null=True)  # type of trail segment (hiking, biking, multi-use, etc.)
    horses = models.BooleanField()  # indicates if horses are allowed on the trail segment
    mileage = models.FloatField(null=True)  # length of the trail segment in miles
    measured_feet = models.FloatField(null=True)  # measured length of trail segment in feet, default/null value of -9999
    dogs = models.BooleanField()  # indicates if dogs are allowed on the trail segment
    st_length = models.FloatField()  # 2D Cartesian length of trail segment in feet, corresponding roughly to mileage
    geometry = models.LineStringField()  # stores trail segment geo data as linestring

    def __str__(self):
        return self.parent_trail.trail_name + " segment " + self.segment_id

