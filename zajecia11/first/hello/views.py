from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.template.loader import get_template


def page(request, num="1"):
    return HttpResponse("page 1")

def template(request):
    t = get_template('helloWord.html')
    html = t.render({})
    return HttpResponse(html)