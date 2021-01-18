from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api import models
import json
import asyncio
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE = 1


@api_view(['POST'])
def run(request):
    STATE = 0
    data = request.POST
    if data['lang'] == "CP":
        f = open(os.path.join(BASE_DIR, 'Codes/main.cpp'), "w")
        f.write(data['code'])
        f.close()
    if data['lang'] == "P3":
        f = open(os.path.join(BASE_DIR, 'Codes/main.py'), "w")
        f.write(data['code'])
        f.close()        

    if('inp' in data.keys() and data['inp'] != None):
        f = open(os.path.join(BASE_DIR, 'Codes/input.txt'), "w")
        f.write(data['inp'])
        f.close()
    os.chdir(os.path.join(BASE_DIR, 'Codes'))
    if data['lang'] == "CP":
        os.system('g++ "main.cpp"')
        os.system('a.exe < input.txt > output.txt')
        os.system('g++ "main.cpp" 2> "output.log"')

    if data['lang'] == "P3":
        os.system('python main.py < input.txt > output.txt 2>"output.log"')

    os.chdir(BASE_DIR)
    out = open(os.path.join(BASE_DIR, 'Codes/output.txt'), "r")
    code_output = out.read()
    f = open(os.path.join(BASE_DIR, 'Codes/input.txt'), "r+")
    f.truncate(0)
    f.close()
    if os.stat(os.path.join(BASE_DIR, "Codes/output.log")).st_size != 0:
        f = open(os.path.join(BASE_DIR, "Codes/output.log"), "r")
        error = f.read()
        models.Submission.objects.filter(pk = data['id']).update(error = error, status = "CE")
        STATE = 1
        return Response()
    else:
        models.Submission.objects.filter(pk = data['id']).update(outputGen = code_output, status = "AC")
        STATE = 1
        return Response()


@api_view(['GET'])
def getstate(request):
    return Response({'state' : STATE})

