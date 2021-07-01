import requests
import ast

from django.shortcuts import render


def index(request):
    url = 'http://127.0.0.1:5000/api-blog-list/'

    try:
        response = requests.get(url)
    except Exception as e:
        return render(request, 'core/body.html', {"error": e})

    print(response)
    if response.status_code == 200:
       print(ast.literal_eval(response.content.decode()).get('blogs'))
    data_to_template = {}

    return render(request, 'core/body.html', data_to_template)