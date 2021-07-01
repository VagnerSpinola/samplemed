import requests
import json
import jwt

from django.shortcuts import render


def index(request):
    url = 'http://127.0.0.1:5000/api-login/'

    params = {'username': request.POST['username'], 'password': request.POST['password']}
    encoded_jwt = jwt.encode(params, "secret", algorithm="HS256")
    print(encoded_jwt)
    try:
        response = requests.post(url, data={"token": encoded_jwt})
    except Exception as e:
        return render(request, 'login/body.html', {"error": e})
    print(response)
    if response.status_code == 202:

        data_to_template = {}
        return render(request, 'core/body.html', data_to_template)
    else:
        data_to_template = {
            "error": "Credenciais nao sao validas"
        }
    return render(request, 'login/body.html', data_to_template)
