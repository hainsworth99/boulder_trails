from django.contrib.gis import admin
from .models import TrailSegment, TrailClosure, Trail

admin.site.register(TrailSegment, admin.GeoModelAdmin)
admin.site.register(TrailClosure, admin.GeoModelAdmin)
admin.site.register(Trail, admin.GeoModelAdmin)
