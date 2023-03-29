from django.shortcuts import render,get_object_or_404
from filtre.models import Division
from filtre.models import Profit_center
from filtre.models import Organisation
import datetime


from django.http import JsonResponse


# Create your views here.


#creation des API

def division_list(request):
 
    divisions = Division.objects.all()
    #json
    #je transforme variable divisions en liste dans un dictionnaire
    #json == dictionnary
    # data ={'Results': list(divisions.values("name","description"))}
    data ={'Results': list(divisions.values("name"))}

    #je dois retourner data en JsonResponse 
    return JsonResponse(data)
    # return render(request,'home/index.html', context)

#ajouter un fichier urls.py dans l'application 
#lier urls de l'application filter au urls du projet


def division_details(request,id):
    division = get_object_or_404(Division,pk=id)
    #result traja3li sous forme dictionary (json)
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
