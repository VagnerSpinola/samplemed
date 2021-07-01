import requests
import json
import jwt
import logging

from django.shortcuts import render, redirect


def index(request):
    if request.method == "POST":
        url = 'http://127.0.0.1:5000/api-login/'
        params = {'username': request.POST['username'], 'password': request.POST['password']}

        encoded_jwt = jwt.encode(params, "secret", algorithm="HS256")
        for i in range(3):
            try:
                response = requests.post(url, data={"token": encoded_jwt})
                break
            except Exception as e:
                return render(request, 'login/body.html', {"error": "Erro por favor tente novamente em instantes"})

        if response.status_code == 202:
            return redirect('core:index')

        return render(request, 'login/body.html', {"error": "Credenciais nao sao validas"})
    return render(request, 'login/body.html', {})