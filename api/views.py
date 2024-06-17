from django.shortcuts import render
import pandas as pd
import json
from django.http import JsonResponse
from .fetch import crypto_df

# Create your views here.

# def current_df_json_response():


def current_df(request):
    
    # data = json.dumps(df.to_dict())
    context = {'json_data': crypto_df}

    return render(request, 'api/current_df.html', context)