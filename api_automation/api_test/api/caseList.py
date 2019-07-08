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
from api_test.models import CaseInfo
from api_test.serializers import CaseSerializer

logger = logging.getLogger(__name__)  # 这里使用 __name__ 动态搜索定义的 logger 配置，这里有一个层次关系的知识点。

class AddCase(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = ()

    def post(self, request):
        """
        添加用例
        """
        data = JSONParser().parse(request)
        case_serializer = CaseSerializer(data=data)
        with transaction.atomic():
            if case_serializer.is_valid():
                case_serializer.save()
                return JsonResponse(data={
                    "case_id": case_serializer.data.get("id")
                }, code="999999", msg="成功")
            else:
                return JsonResponse(code="999998", msg="失败")


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