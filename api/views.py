from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Submission
from problem.models import Problem
import json
import asyncio
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE = 1


@api_view(['POST'])
def run(request):
    data = request.POST
    probId = data['problemId']
    totaltc = Problem.objects.get(id = probId).totalTC
    if data['lang'] == "CP":
        f = open(os.path.join(BASE_DIR, 'Codes/main.cpp'), "w")
        f.write(data['code'])
        f.close()
    if data['lang'] == "P3":
        f = open(os.path.join(BASE_DIR, 'Codes/main.py'), "w")
        f.write(data['code'])
        f.close()        
    isInputGiven = False
    if('inp' in data.keys() and data['inp'] != None):
        isInputGiven = True
        f = open(os.path.join(BASE_DIR, 'Codes/input.txt'), "w")
        f.write(data['inp'])
        f.close()
    os.chdir(os.path.join(BASE_DIR, 'Codes'))
    if data['lang'] == "CP":
        os.system('g++ "main.cpp"')
        cnt = 0
        if(isInputGiven == False):
            for i in range(1, totaltc+1):
                isSame = True
                inpPath = os.path.join(BASE_DIR, "media", 'TestCases', probId, 'input'+str(i)+'.txt')
                os.system(f'./a.out < {inpPath} > output.txt')
                with open(os.path.join(BASE_DIR, "media", 'TestCases', probId, 'output'+str(i)+'.txt')) as f1, open('output.txt') as f2:
                    for line1, line2 in zip(f1, f2):
                        if line1 != line2:
                            isSame = False
                            break
                if(isSame):
                    cnt += 1
            f = open(os.path.join(BASE_DIR, 'Codes/output.txt'), "r+")
            f.truncate(0)
            f.close()
        else:
            os.system('./a.out < input.txt > output.txt')
        
        os.system('g++ "main.cpp" 2> "output.log"')

    if data['lang'] == "P3":
        os.system('python main.py < input.txt > output.txt 2>"output.log"')

    os.chdir(BASE_DIR)
    out = open(os.path.join(BASE_DIR, 'Codes/output.txt'), "r")
    code_output = out.read()
    f = open(os.path.join(BASE_DIR, 'Codes/input.txt'), "r+")
    f.truncate(0)
    f.close()
    tcString = str(cnt) + "/" + str(totaltc)
    if os.stat(os.path.join(BASE_DIR, "Codes/output.log")).st_size != 0:
        f = open(os.path.join(BASE_DIR, "Codes/output.log"), "r")
        error = f.read()
        Submission.objects.filter(pk = data['id']).update(error = error, status = "CE", testCasesPassed = tcString)
        return Response()
    else:
        Submission.objects.filter(pk = data['id']).update(outputGen = code_output, status = "AC", testCasesPassed = tcString)
        return Response()


@api_view(['GET'])
def getstate(request):
    return Response({'state' : STATE})

