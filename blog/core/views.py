import requests
import ast

from django.shortcuts import render


def index(request):
    url = 'http://127.0.0.1:5000/api-blog-list/'
    for i in range(3):
        try:
            response = requests.get(url)
            break
        except Exception as e:
            return render(request, 'login/body.html', {"error": "Erro por favor tente novamente em instantes"})

    if response.status_code == 200:
        return render(request, 'core/body.html', ast.literal_eval(response.content.decode()))