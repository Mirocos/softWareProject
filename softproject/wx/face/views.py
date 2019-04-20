from django.shortcuts import render
from django.http import HttpResponse
from wx.face.cat_test import get_pred
# Create your views here.


def index(request):
    list = get_pred()
    return HttpResponse(list)


