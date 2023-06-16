import os
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
import numpy as np
from io import StringIO
import psycopg2
import json

from django.db.models import Sum


from rest_framework.decorators import api_view
from django.http import JsonResponse
import requests
from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_exempt
import datetime
from os.path import exists
from order_past.models import *
from .serializers import Order_past_per_divsionSerializer
from .serializers import Order_past_per_organismeSerializer
from .serializers import Order_past_per_cpSerializer
from .serializers import Order_past_per_errorsSerializer


import traceback
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order_past_per_divsion

import os


@csrf_exempt
def save_file(request):
    for f in ["ccclient","cepc","tcurr"]:
        file=request.FILES[f]
        file_name = default_storage.save(file.name,file)
        os.system("chmod -R 777 /media")

    return JsonResponse({}, safe=False)


@api_view(['GET'])
def select_files(request, year, week):
    conn = psycopg2.connect(host=os.getenv('PG_HOST', "localhost"),
                            dbname=os.getenv('PG_DB', "dashboard_db"),
                            user=os.getenv('PG_USER', "postgres"),
                            password=os.getenv('PG_PASSWORD', "khouloud123"),
                            port=os.getenv('PG_PORT', "5432")) 
    
    cur = conn.cursor()
    cur.execute("SET datestyle=DMY;")

    # Files
    if week < 10:
       week=str(0)+str(week)
    

    file_cclient = f'{os.getcwd()}media/CCCLIENT_{year}{week}.txt'
    file_cepc = f'{os.getcwd()}media/CEPC_{year}{week}.XLSX'
    file_tcurr = f'{os.getcwd()}media/TCURR_{year}{week}.XLSX'

    cclient_exists = exists(file_cclient)
    cepc_exists = exists(file_cepc)
    tcurr_file_exists=exists(file_tcurr)

    message_error= ''
    if cclient_exists == False:
        message_error= f'Unable to find CCLIENT File, {file_cclient} not exist or unreadable!'
        return JsonResponse(message_error, status=status.HTTP_500_INTERNAL_SERVER_ERROR, safe=False)
    
    if cepc_exists == False:
        message_error= f'Unable to find CEPC File, {file_cepc} not exist or unreadable!'
        return JsonResponse(message_error, status=status.HTTP_500_INTERNAL_SERVER_ERROR, safe=False)

    if tcurr_file_exists == False:
        message_error= f'Unable to find TCURR File, {file_tcurr} not exist or unreadable!'
        return JsonResponse(message_error, status=status.HTTP_500_INTERNAL_SERVER_ERROR, safe=False)

    nettoyage_files(conn,week,year,file_cclient,file_cepc,file_tcurr)

    return JsonResponse("ok", status=status.HTTP_200_OK, safe=False)




""" @api_view(['POST'])
def cclient_save(request, year, week):
 #Set Column name for file_cclient
    colnames=['1',
    'Don.ordre',
    'ClientLivré',
    '2',
    '3',
    'NºCdeClient',
    '4',
    '5',
    'PosClt',
    'Ech.Clt',
    'DateCdeClient',
    'Dev.',
    'N CdePrev',
    'PosPrev',
    'ArticleInterne',
    'ArticleClient',
    '6',
    'Designation1',
    'Qté',
    'OTP',
    'MSN',
    'N SérieDébut',
    'N SérieFin',
    'Prix net',
    'DtLv.Souh.',
    'NonFact.',
    'Rf',
    'BF',
    'BL',
    'Désignation2',
    'Désignation3',
    'Désignation4',
    'Désignation5',
    'Memo',
    'Remarque1',
    'Remarque2',
    'Remarque3',
    'PointDéchargement',
    'Destinataire',
    'Pri',
    'Inctm',
    'Incoterms2',
    'CPmt',
    'GrI',
    'TaxD',
    'NoteEntete',
    'N Contrat',
    'Div.',
    'Itin.',
    'N CdeSAP',
    'PosteSAP',
    'TyPo',
    'N CdeSILOG',
    'PosSILOG',
    'SG',
    'SL',
    'Dtlivr.Ech.',
    'QtécdéeEch.',
    'QtéConf.Ech.',
    'CtrPr',
    'Sort.March',
    'OrgCm',
    ]
    #Read File
    file_cclient = f'{os.getcwd()}\media\CCCLIENT_{year}{week}.txt'
   
    df=pd.read_csv(file_cclient, encoding='utf-16', sep='\t',names=colnames)


    df['Designation1']=df['Designation1'].str.replace(';',',')

    #PB FCA in Col Prix 
    df=df[df['Prix net'] != 'FCA']


    #Drop first 13 cols
    df=df.drop(list(range(14))).reset_index()
    #Drop unused col 
    df=df.drop(columns=['index','1','2','3','4','5','6'])
    #Drop empty rows 
    df=df.dropna(how='all')
    #Drop  the repetitive lines that contain Don. ordre
    df=df[(df["Don.ordre"].str.contains("Don. ordre")==False)]

    df['QtécdéeEch.']=df['QtécdéeEch.'].str.strip()
    df['QtécdéeEch.']=df['QtécdéeEch.'].str.replace(",",".")
    df['QtécdéeEch.']=df['QtécdéeEch.'].str.replace(" ","")
    df['QtéConf.Ech.']=df['QtéConf.Ech.'].str.strip()
    df['QtéConf.Ech.']=df['QtéConf.Ech.'].str.replace(",",".")
    df['QtéConf.Ech.']=df['QtéConf.Ech.'].str.replace(" ","")

    print(df)

    return JsonResponse(df.to_json(), safe=False)

 """



def nettoyage_files(conn,week,year,file_cclient,file_cepc,file_tcurr):

    #--------------------------------------------------------------------------------
    #Set Column name for file_cclient
    colnames=['1',
    'Don.ordre',
    'ClientLivré',
    '2',
    '3',
    'NºCdeClient',
    '4',
    '5',
    'PosClt',
    'Ech.Clt',
    'DateCdeClient',
    'Dev.',
    'N CdePrev',
    'PosPrev',
    'ArticleInterne',
    'ArticleClient',
    '6',
    'Designation1',
    'Qté',
    'OTP',
    'MSN',
    'N SérieDébut',
    'N SérieFin',
    'Prix net',
    'DtLv.Souh.',
    'NonFact.',
    'Rf',
    'BF',
    'BL',
    'Désignation2',
    'Désignation3',
    'Désignation4',
    'Désignation5',
    'Memo',
    'Remarque1',
    'Remarque2',
    'Remarque3',
    'PointDéchargement',
    'Destinataire',
    'Pri',
    'Inctm',
    'Incoterms2',
    'CPmt',
    'GrI',
    'TaxD',
    'NoteEntete',
    'N Contrat',
    'Div.',
    'Itin.',
    'N CdeSAP',
    'PosteSAP',
    'TyPo',
    'N CdeSILOG',
    'PosSILOG',
    'SG',
    'SL',
    'Dtlivr.Ech.',
    'QtécdéeEch.',
    'QtéConf.Ech.',
    'CtrPr',
    'Sort.March',
    'OrgCm',
    ]
    #Read Files
    df=pd.read_csv(file_cclient,encoding='UTF-16 LE',sep='\t',names=colnames, low_memory=False)
    df_cepc=pd.read_excel(file_cepc)
    df_tcurr=pd.read_excel(file_tcurr)

    df_tcurr=df_tcurr[df_tcurr['Type de cours']=='M']
    df_tcurr=df_tcurr[df_tcurr['Devise cible']=='EUR']
    df_tcurr_last=df_tcurr.groupby(['Dev. source'])['Taux'].first().reset_index() 


    df['Designation1']=df['Designation1'].str.replace(';',',')

    #PB FCA in Col Prix 
    df=df[df['Prix net'] != 'FCA']


    #Drop first 13 cols
    df=df.drop(list(range(14))).reset_index()
    #Drop unused col 
    df=df.drop(columns=['index','1','2','3','4','5','6'])
    #Drop empty rows 
    #Drop  the repetitive lines that contain Don. ordre
    df=df[(df["Don.ordre"].str.contains("Don. ordre")==False)]

    df['QtécdéeEch.']=df['QtécdéeEch.'].str.strip()
    df['QtécdéeEch.']=df['QtécdéeEch.'].str.replace(",",".")
    df['QtécdéeEch.']=df['QtécdéeEch.'].str.replace(" ","")
    df['QtéConf.Ech.']=df['QtéConf.Ech.'].str.strip()
    df['QtéConf.Ech.']=df['QtéConf.Ech.'].str.replace(",",".")
    df['QtéConf.Ech.']=df['QtéConf.Ech.'].str.replace(" ","")

    # Get design centre de profit from cepc file
    dict_cp_cepc=dict(zip(df_cepc['Centre de profit'],df_cepc['Désing. centre de pro.']))
    df['design_centre_profit']=df['CtrPr'].map(dict_cp_cepc)
    df['Designation CP']=df['CtrPr'].astype(str)+'-'+df['design_centre_profit'].astype(str)

    # Get design centre de profit from cepc file
    dict_resp_cp_cepc=dict(zip(df_cepc['Centre de profit'],df_cepc['Responsable centre de profit']))
    df['Program responsible']=df['CtrPr'].map(dict_resp_cp_cepc)

    # Get rate from TCURR
    dict_rate_tcuur=dict(zip(df_tcurr_last['Dev. source'],df_tcurr_last['Taux']))
    df['rate']=df['Dev.'].map(dict_rate_tcuur)
    df['rate']=df['rate'].str.replace('/','')
    df['rate']=df['rate'].str.replace(',','.')
    df['rate']=df['rate'].astype(float)
    df['rate']=np.where(df['Dev.']=='EUR',1,df['rate'])

    #Convert Prix net to float
    df['Prix net']=df['Prix net'].str.replace(',','.')
    df['Prix net']=df['Prix net'].str.replace(' ','')
    df['Prix net']=df['Prix net'].fillna(0)
    df['Prix net']=df['Prix net'].astype(float)

    #Convert Qté net to float
    df['Qté']=df['Qté'].str.replace(',','.')
    df['Qté']=df['Qté'].str.replace(' ','')
    df['Qté']=df['Qté'].astype(float)

    #Price Euro Calculte => Formula: Prix net * rate / Qté
    df['price_euro']=df['Qté'] * df['Prix net'] / df['rate']

    #Get Monday
    # date=file_cclient.split('_')[1].removesuffix('.txt')
    # date=date[:4]+'-W'+date[4:]
    date=str(year)+'-W'+str(week)
    monday=datetime.datetime.strptime(date+'-1','%Y-W%W-%w')
    df['monday']=monday
    df['diff_date']=(pd.to_datetime(df['DtLv.Souh.'],format='%d.%m.%Y',errors='coerce')-df['monday']).dt.days
    df['past_status']=np.where(df['diff_date'] > -30,'less than one month in the past','gt than one month in the past')
    df['past_status']=np.where(df['diff_date'] > 0,'Not in the past',df['past_status'])

    df['Error Bill vs Price']=np.where(((df['NonFact.']=='X') & (df['Prix net'] > 0)) | (((df['NonFact.'].isna())) & (df['Prix net'] == 0)),'Program: Error Bill vs Price','')
    df['Error Routes']=np.where(( (df['Itin.'].isna())& (df['ArticleInterne'].str.startswith('IS')) ),'Planif: Error Routes','')

    df['Error type']=df['Error Bill vs Price'].astype(str)+' '+ df['Error Routes'].astype(str)
    # df['Error type']=df['Error type'].str.strip()
    df.insert(0,'year',year,True)
    df.insert(1,'week',week,True)
    df=df.drop(columns=['Remarque1', 'Remarque2','Remarque3','PointDéchargement','Memo'])

    #Orders in the past
    df_past=df[df['diff_date'] < 0]

    #Order by division
    order_past_per_divsion=df_past.groupby(['year','week','Div.']).agg({'Don.ordre':'count','price_euro':'sum'}).reset_index()

    #Order by Organisme
    order_past_per_organisme=df_past.groupby(['year','week','OrgCm']).agg({'Don.ordre':'count','price_euro':'sum'}).reset_index()

    #Order by division
    order_past_per_cp=df_past.groupby(['year','week','CtrPr']).agg({'Don.ordre':'count','price_euro':'sum'}).reset_index()

    #Order by errors
    order_past_per_errors=df_past.groupby(['year','week','Error type']).agg({'Don.ordre':'count','price_euro':'sum'}).reset_index()
    order_past_per_errors['Error type']=order_past_per_errors['Error type'].str.strip()
    # order_past_per_errors=order_past_per_errors[order_past_per_errors['Error type'].notnull()]
    order_past_per_errors=order_past_per_errors[order_past_per_errors['Error type'].str.contains('Error')]

    #Save order_past_per_divsion to DB
    division_data = StringIO()
    division_data.write(order_past_per_divsion.to_csv( header=None, index=False ,sep=';'))
    # This will make the cursor at index 0
    division_data.seek(0)
    with conn.cursor() as c:
        c.copy_from(
            file=division_data,
            #file name in DB
            table="order_past_order_past_per_divsion",
            columns=[
                'year',
                'week',
                'division',
                'count',
                'price',
            ],
            null="",
            sep=";",
        )

    conn.commit()

    #Save order_past_per_organisme to DB
    organisme_data = StringIO()
    organisme_data.write(order_past_per_organisme.to_csv( header=None, index=False ,sep=';'))
    # This will make the cursor at index 0
    organisme_data.seek(0)
    with conn.cursor() as c:
        c.copy_from(
            file=organisme_data,
            #file name in DB
            table="order_past_order_past_per_organisme",
            columns=[
                'year',
                'week',
                'organisme',
                'count',
                'price',
            ],
            null="",
            sep=";",
        )

    conn.commit()

        #Save order_past_per_cp to DB
    cp_data = StringIO()
    cp_data.write(order_past_per_cp.to_csv( header=None, index=False ,sep=';'))
    # This will make the cursor at index 0
    cp_data.seek(0)
    with conn.cursor() as c:
        c.copy_from(
            file=cp_data,
            #file name in DB
            table="order_past_order_past_per_cp",
            columns=[
                'year',
                'week',
                'cp',
                'count',
                'price',
            ],
            null="",
            sep=";",
        )

    conn.commit()

            #Save order_past_per_errors to DB
    errors_data = StringIO()
    errors_data.write(order_past_per_errors.to_csv( header=None, index=False ,sep=';'))
    # This will make the cursor at index 0
    errors_data.seek(0)
    with conn.cursor() as c:
        c.copy_from(
            file=errors_data,
            #file name in DB
            table="order_past_order_past_per_errors",
            columns=[
                'year',
                'week',
                'error',
                'count',
                'price',
            ],
            null="",
            sep=";",
        )

    conn.commit()


    #Save details to DB
    all_data = StringIO()
    #convert file to csv
    all_data.write(df.to_csv( header=None, index=False ,sep=';'))
    # This will make the cursor at index 0
    all_data.seek(0)
    with conn.cursor() as c:
        c.copy_from(
            file=all_data,
            #file name in DB
            table="order_past_order_files",
            columns=[
                'year',
                'week',
                'don_ordre',
                'clientLivre',
                'n_CdeClient',
                'PosClt',
                'Ech_Clt',
                'DateCdeClient',
                'Dev',
                'n_CdePrev',
                'PosPrev',
                'ArticleInterne',
                'ArticleClient',
                'Designation1',
                'Qte',
                'OTP',
                'MSN',
                'n_SerieDebut',
                'n_SerieFin',
                'Prix_net',
                'DtLv_Souh',
                'NonFact',
                'Rf',
                'BF',
                'BL',
                'Designation2',
                'Designation3',
                'Designation4',
                'Designation5',
                # 'Memo',
                # 'Remarque1',
                # 'Remarque2',
                # 'Remarque3',
                # 'PointDechargement',
                'Destinataire',
                'Pri',
                'Inctm',
                'Incoterms2',
                'CPmt',
                'GrI',
                'TaxD',
                'NoteEntete',
                'n_Contrat',
                'Div',
                'Itin',
                'n_CdeSAP',
                'PosteSAP',
                'TyPo',
                'n_CdeSILOG',
                'PosSILOG',
                'SG',
                'SL',
                'Dtlivr_Ech',
                'QtecdeeEch',
                'QteConf_Ech',
                'CtrPr',
                'Sort_March',
                'OrgCm',
                'design_centre_profit',
                'Designation_CP',
                'Program_responsible',
                'rate',
                'price_euro',
                'monday',
                'diff_date',
                'past_status',
                'Error_Bill_vs_Price',
                'Error_Routes',
                'Error_type',
            ],
            null="",
            sep=";",
        )

    conn.commit()


def traitement(request):

    try:
        username=request.META['REMOTE_USER']
    except:
        username=''

    current_week=datetime.datetime.now().isocalendar().week
    current_year=datetime.datetime.now().isocalendar().year
 
    #Get Data from DB

    order_past_per_divsion=Order_past_per_divsion.objects.all().filter(year=current_year,week=current_week)
    details_order_past_per_divsion=order_past_per_divsion.aggregate( Sum('price'),Sum('count') ) 

    order_past_per_organisme=Order_past_per_organisme.objects.all().filter(year=current_year,week=current_week).order_by('-count')
    details_order_past_per_organisme=order_past_per_organisme.aggregate( Sum('price'),Sum('count') ) 

    order_past_per_cp=Order_past_per_cp.objects.all().filter(year=current_year,week=current_week).order_by('-count')[:10]
    details_order_past_per_cp=order_past_per_cp.aggregate( Sum('price'),Sum('count') )

    order_past_per_errors=Order_past_per_errors.objects.all().filter(year=current_year,week=current_week).order_by('-count')
    details_order_past_per_errors=order_past_per_errors.aggregate( Sum('price'),Sum('count') ) 
    
  # select count(*) from Order_files
    count=Order_files.objects.all().count()
    cost=Order_files.objects.aggregate( Sum('price_euro'))

    print(count)
    # Create Dictionary
    value = {
        "count": count,
    }

    print(value.get('count'))

    # Dictionary to JSON Object using dumps() method
    # Return JSON Object
    return JsonResponse(value)


def count(request):
 #select count(*) from Order_files
    count=Order_files.objects.all().count()

    print(count)
    # Create Dictionary
    value = {
        "count": count,
    }

    print(value.get('count'))

    # Dictionary to JSON Object using dumps() method
    # Return JSON Object
    return JsonResponse(value)

def cost(request):
 #select count(*) from Order_files
    cost=Order_files.objects.aggregate( Sum('price_euro'))

    print(cost)
    # Create Dictionary
    valuecost = {
        "cost": cost,
    }

    print(valuecost.get('cost'))

    # Dictionary to JSON Object using dumps() method
    # Return JSON Object
    return JsonResponse(valuecost)



@api_view(('GET',))
def count_order_par_division(request, *args, **kwargs):
    if request.method == 'GET':
        queryset2 = Order_past_per_divsion.objects.all()
        serializer = Order_past_per_divsionSerializer(queryset2, many=True)
        return Response(serializer.data)

@api_view(('GET',))
def order_par_organisme(request):
    if request.method == 'GET':
        try:
            queryset3 = Order_past_per_organisme.objects.all()
            # print(queryset3)
            serializer = Order_past_per_organismeSerializer(queryset3, many=True)
            # print(serializer.data)
            return Response(serializer.data)
        except:
            traceback.print_stack()


@api_view(('GET',))
def order_par_cp(request, *args, **kwargs):
    if request.method == 'GET':
        queryset2 = Order_past_per_cp.objects.all()
        serializer = Order_past_per_cpSerializer(queryset2, many=True)
        return Response(serializer.data)
    

@api_view(('GET',))
def order_par_errors(request, *args, **kwargs):
    if request.method == 'GET':
        queryset2 = Order_past_per_errors.objects.all()
        serializer = Order_past_per_errorsSerializer(queryset2, many=True)
        return Response(serializer.data)