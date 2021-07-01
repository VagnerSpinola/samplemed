import requests
import json

from django.shortcuts import render


def index(request):
    url = 'http://127.0.0.1:8000/api-login'

    params = {'username': request.POST['username'], 'password': request.POST['password']}
    headers = {'content-type': 'application/json'}

    try:
        response = requests.post(url, params=params, headers=headers)
    except Exception as e:
        data_to_template = {
            "error": e
        }
        return render(request, 'login/body.html', data_to_template)

    if response.status_code == 200:
        data_to_template = {}
    else:
        data_to_template = {
            "error": "Credenciais nao sao validas"
        }
    return render(request, 'login/body.html', data_to_template)
