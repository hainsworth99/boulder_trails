from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Trail, TrailSegment, TrailClosure

def trails(request):

    return HttpResponse(serialize('geojson', TrailSegment.objects.all()))

