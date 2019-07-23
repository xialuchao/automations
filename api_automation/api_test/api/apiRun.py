import requests
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.utils import json

host = "192.168.0.42"
# httpType = "http:"
def apiRun(httpType, headers, data, path, host="192.168.0.42"):
    if httpType == "HTTP":
        httpType = "http:"
    elif httpType == "HTTPS":
        httpType = "https:"
    # headers = {'X-ZhaoTest-UserId':'1000010'}
    # data = {'isHot':'1', 'page':'1', 'size':'10'}
    # path = '/categoryquotation'
    print(httpType + "//" + host + path)
    r = requests.get(httpType + "//" + host + path, data=data, headers=headers)
    print(r.text)