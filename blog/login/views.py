import requests
import json
import jwt

from django.shortcuts import render, redirect


def index(request):
    if request.method == "POST":
        url = 'http://127.0.0.1:5000/api-login/'
        params = {'username': request.POST['username'], 'password': request.POST['password']}

        encoded_jwt = jwt.encode(params, "secret", algorithm="HS256")

        try:
            response = requests.post(url, data={"token": encoded_jwt})
        except Exception as e:
            return render(request, 'login/body.html', {"error": e})

        if response.status_code == 202:
            return redirect('core:index')

        return render(request, 'login/body.html', {"error": "Credenciais nao sao validas"})
    return render(request, 'login/body.html', {})