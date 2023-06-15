from django.shortcuts import render,get_object_or_404
from filtre.models import Division
from filtre.models import Profit_center
from filtre.models import Organisation
from django.db.models import Q

import datetime
from rest_framework import viewsets
from filtre.serializers import DivisionSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import json
from order_past.models import Order_past_per_divsion
from order_past.models import Order_past_per_cp
from order_past.models import Order_past_per_organisme

from django.db.models import Sum


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

@csrf_exempt
def filtre_result(request):
  
    json_body = json.loads(request.body)
    

    order_past_per_divsion = Order_past_per_divsion.objects.all()
    order_past_per_cp = Order_past_per_cp.objects.all()
    order_past_per_organisme = Order_past_per_organisme.objects.all()



    division = json_body.get("division")
    print (division)
    
    if division:
        query = Q(division=division[0])
        for div in division:
            query = query | Q(division=div)

    if query:
        order_past_per_divsion = order_past_per_divsion.filter(query)




    profit_center = json_body.get("profit_center")
    print (profit_center)

    if profit_center:
        query_cp = Q(cp=profit_center[0])
        for item in profit_center:
            query_cp = query_cp | Q(cp=item)

    if query_cp:
        order_past_per_cp = order_past_per_cp.filter(query_cp)




    organisation = json_body.get("organisation")
    print (organisation)

    if organisation:
        query_organisme = Q(organisme=organisation[0])
        for item in organisation:
            query_organisme = query_organisme | Q(organisme=item)

    if query_organisme:
        order_past_per_organisme = order_past_per_organisme.filter(query_organisme)




    week_year = json_body.get("week_year")
    print (week_year)
    
    if week_year:
        new_list = week_year[0].split("_")
        query_week_year = Q(week=new_list[0], year=new_list[1])
        for item in week_year:  
                new_list = item.split("_")
                print(new_list)
                query_week_year = query_week_year | Q(week=new_list[0], year=new_list[1])
    if query_week_year:
        order_past_per_divsion = order_past_per_divsion.filter(query_week_year)
        order_past_per_cp = order_past_per_cp.filter(query_week_year)
        order_past_per_organisme = order_past_per_organisme.filter(query_week_year)

        
    
   

    # return JsonResponse()
    data = {}
    data['division'] = list(order_past_per_divsion.values())
    data['profit_center'] = list(order_past_per_cp.values())
    data['organisation'] = list(order_past_per_organisme.values())


    return JsonResponse(data, safe=False)



