from django.shortcuts import render


def index(request):
    data_to_template = {}
    return render(request, 'core/body.html', data_to_template)