from django.shortcuts import render,get_object_or_404
from filtre.models import Division
from filtre.models import Profit_center
from filtre.models import Organisation
import datetime
from rest_framework import viewsets
from filtre.serializers import DivisionSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


# Create your views here.


""" class DivisionSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    #on filtre sur des champs specifiques
    filterset_fields = ['name']
    search_fields = ['name'] """
#creation des API

""" @csrf_exempt
def DivisionAPI(request):
    if request.method=='GET':
        divisions = Division.objects.all()
        division_serializer = DivisionSerializer(divisions, many=True)
        return JsonResponse(division_serializer.data, safe=False)
    elif request.method == 'POST':
        division_data=JSONParser().parse(request)
        division_serializer = DivisionSerializer(data=division_data)
        if division_serializer.is_valid():
            division_serializer.save()
            return JsonResponse("Added Sucessfully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        division_data =JSONParser().parse(request)
        division= Division.objects.get(name=division_data['name'])
        division_serializer=DivisionSerializer(division,data=division_data)
        if division_serializer.is_valid():
            division_serializer.save()
            return JsonResponse("Update Sucessfully!!", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        division= Division.objects.get(name=Division.name)
        division.delete()
        return JsonResponse("Deleted Sucessfully!!", safe=False) """






def division_list(request):
 
    divisions = Division.objects.all()
    data ={'Results': list(divisions.values("name"))}
    return JsonResponse(data)



def division_details(request,id):
    division = get_object_or_404(Division,pk=id)
    data = { 'Results': {
        "name":division.name,
        "description":division.description } }
    return JsonResponse(data)



def profit_list(request):
 
    profits = Profit_center.objects.all()
    data ={'Results': list(profits.values("name"))}
    return JsonResponse(data)

def organisation_list(request):
 
    organisations = Organisation.objects.all()
    data ={'Results': list(organisations.values("name"))}
    return JsonResponse(data)


def filter_range(request):
    current_week=datetime.datetime.now().isocalendar().week
    current_year=datetime.datetime.now().isocalendar().year

    weeks_per_year = 52
    last_numbers = 12

    last_n = []
    for i in range(current_week, (current_week - last_numbers) , -1):
        if i <= 0:
            week = i + weeks_per_year
            year = current_year - 1
        else:
            week = i
            year = current_year
        result = f"{week}_{year}"
        last_n.append(result)

    return JsonResponse(last_n, safe=False)



