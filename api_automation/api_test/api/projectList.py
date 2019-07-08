import logging

from crontab import CronTab
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView


from api_test.common.api_response import JsonResponse
from api_test.models import Project
from api_test.serializers import ProjectSerializer, ProjectDeserializer, \
    ProjectMemberDeserializer

logger = logging.getLogger(__name__)  # 这里使用 __name__ 动态搜索定义的 logger 配置，这里有一个层次关系的知识点。


class ProjectList(APIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = ()

    def get(self, request):
        """
        获取项目列表
        :param request:
        :return:
        """
        try:
            page_size = int(request.GET.get("page_size", 20))
            page = int(request.GET.get("page", 1))
        except (TypeError, ValueError):
            return JsonResponse(code="999985", msg="page and page_size must be integer!")
        # name = request.GET.get("name")
        # if name:
        #     obi = Project.objects.filter(name__contains=name).order_by("id")
        # else:
        obi = Project.objects.all().order_by("id")
        paginator = Paginator(obi, page_size)  # paginator对象
        total = paginator.num_pages  # 总页数
        # try:
        obm = paginator.page(page)
        # except PageNotAnInteger:
        #     obm = paginator.page(1)
        # except EmptyPage:
        #     obm = paginator.page(paginator.num_pages)
        serialize = ProjectSerializer(obm, many=True)
        return JsonResponse(data={"data": serialize.data,
                                  "page": page,
                                  "total": total
                                  }, code="999999", msg="成功")

class AddProject(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = ()

    def post(self, request):
        """
        新增项目
        :param request:
        :return:
        """
        data = JSONParser().parse(request)
        project_serializer = ProjectDeserializer(data=data)
        with transaction.atomic():
            if project_serializer.is_valid():
                # 保持新项目
                project_serializer.save()
                return JsonResponse(data={
                        "project_id": project_serializer.data.get("id")
                    }, code="999999", msg="成功")
            else:
                return JsonResponse(code="999998", msg="失败")

class DelProject(APIView):
    """
    删除项目
    """
    def delete(self, request):
        data = JSONParser().parse(request)
        j = data["ids"]
        obj = Project.objects.filter(id=j)
        print(j)
        obj.delete()
        # my_user_cron = CronTab(user=True)
        # my_user_cron.remove_all(comment=j)
        # my_user_cron.write()
        return JsonResponse(code="999999", msg="成功")

