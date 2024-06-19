from django.shortcuts import render
import pandas as pd
import json
from django.http import JsonResponse
from .fetch import api_exec

import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects



# def api_exec2():

#     try:
#         url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
#         headers = {
#             'Accepts': 'application/json',
#             'X-CMC_PRO_API_KEY': 'c6b393db-6b8c-4faf-8cb5-4e918e116472',
#         }
#         response = requests.get(url, headers=headers)
#         data = response.json()
    
#     except (ConnectionError, Timeout, TooManyRedirects) as e: 
        
#         file_path = 'data.json'

#         with open(file_path, 'r') as file:
#             data = json.load(file)

#             print(f"LOCAL DATA:\n {data}")
#             return data['data']


#     return data['data']


# def current_df(request):
    
#     if 'crypto_data' not in request.session:
#         data = api_exec2()
#         print(json.dumps(data, indent=2))
#         request.session['crypto_data'] = data
#     else:
#         data = request.session['crypto_data']


#     # data = json.dumps(df.to_dict())
#     context = {'json_data': data}

#     return render(request, 'api/current_df.html', context)



def current_df(request):
    
    data = api_exec()
    # print(json.dumps(data, indent=2))

    # data = json.dumps(df.to_dict())
    context = {'json_data': data}
    

    return render(request, 'api/current_df.html', context)