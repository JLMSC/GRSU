from django.shortcuts import render
from django.http import JsonResponse

from Main import main


def index(request):
    resp_dict = main()
    return JsonResponse(resp_dict)