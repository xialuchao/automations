import logging

import time
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction
from django.db.models import Q
from django.http import StreamingHttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from api_test.common.api_response import JsonResponse
from api_test.models import CaseInfo, ApiInfo
from api_test.serializers import CaseSerializer, ApiInfoSerializer, ApiInfoDeserializer, ApiGroupLevelFirstSerializer, ApiInfoSerializer, APIRequestHistorySerializer, \
    ApiOperationHistorySerializer, ApiInfoListSerializer, ApiInfoDocSerializer, ApiGroupLevelFirstDeserializer, \
    ApiInfoDeserializer, ApiHeadDeserializer, ApiParameterDeserializer, \
    ApiResponseDeserializer, APIRequestHistoryDeserializer, ProjectSerializer

logger = logging.getLogger(__name__)  # 这里使用 __name__ 动态搜索定义的 logger 配置，这里有一个层次关系的知识点。

class AddCase(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = ()

    def post(self, request):
        """
        添加用例
        """
        # data = JSONParser().parse(request)
        # case_serializer = CaseSerializer(data=data)
        # print(case_serializer)
        # with transaction.atomic():
        #     if case_serializer.is_valid():
        #         case_serializer.save()
        #         return JsonResponse(data={
        #             "case_id": case_serializer.data.get("id")
        #         }, code="999999", msg="成功")
        #     else:
        #         return JsonResponse(code="999998", msg="失败")

        data = JSONParser().parse(request)
        obj = Project.objects.get(id=data["project_id"])
        api_name = ApiInfo.objects.filter(name=data["name"],project=data["project_id"])
        if len(api_name):
            return JsonResponse(code="999997", msg="用例名已存在，请更改")
        else:
            with transaction.atomic(): # 执行错误后，帮助事务回滚
                serialize = ApiInfoDeserializer(data=data)
                if serialize.is_valid():
                    api_id = serialize.data.get("id")
                    if len(data.get("headDict")):
                        for i in data["headDict"]:
                            i["api"] = api_id
                            head_serialize = ApiHeadDeserializer(data=i)
                            if head_serialize.is_valid():
                                head_serialize.save(api=ApiInfo.objects.get(id=api_id))
                    if len(data.get("requestList")):
                        for i in data["requestList"]:
                            if i.get("name"):
                                i["api"] = api_id
                                param_serialize = ApiParameterDeserializer(data=i)
                                if param_serialize.is_valid():
                                    param_serialize.save(api=ApiInfo.objects.get(id=api_id))
                    if len(data.get("responseList")):
                        for i in data["responseList"]:
                            if i.get("name"):
                                i["api"] = api_id
                                response_serialize = ApiResponseDeserializer(data=i)
                                if response_serialize.is_valid():
                                    response_serialize.save(api=ApiInfo.objects.get(id=api_id))
                    return JsonResponse(code="999999", msg="成功!", data={"api_id": api_id})
                return JsonResponse(code="999996", msg="参数有误!")


class GetCase(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = ()

    def get(self, request):
        """
        获取用例接口参数
        """
        try:
            page_size = int(request.GET.get("page_size", 20))
            page = int(request.GET.get("page", 1))
        except (TypeError, ValueError):
            return JsonResponse(code="999985", msg="page and page_size must be integer!")
        obi = CaseInfo.objects.all().order_by("id")
        paginator = Paginator(obi, page_size)  # paginator对象
        total = paginator.num_pages  # 总页数
        obm = paginator.page(page)
        serialize = CaseSerializer(obm, many=True)
        return JsonResponse(data={"data": serialize.data,
                                  "page": page,
                                  "total": total
                                  }, code="999999", msg="成功")