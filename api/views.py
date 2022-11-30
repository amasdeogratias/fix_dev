from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Location
from .serializers import LocationSerializer
from django.db.models import Q

# Create your views here.
@api_view(['GET'])
def endpoints(request):
    data = ['/locations','locations/:name']
    return Response(data)
 
@api_view(['GET', 'POST'])    
def location_list(request):
    # Handle GET request
    if request.method=='GET':
        
        # /search option in list
        # /locations/?query=Pune
        query = request.GET.get('query')
        
        if query == None:
            query=''
        #single and multiple search
        locations = Location.objects.filter(Q(name__icontains=query)| Q(latitude__icontains=query))
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)
        
    # Handle POST request
    if request.method == 'POST':
        location = Location.objects.create(
            name = request.data['name'],
            latitude=request.data['latitude'],
            longitude=request.data['longitude']
        )
        serializer = LocationSerializer(location, many=False)
        return Response(serializer.data)
        
    
# return single location by name
@api_view(['GET'])
def location_detail(request,name):
    locations = Location.objects.get(name=name)
    serializer = LocationSerializer(locations, many=False)
    return Response(serializer.data)