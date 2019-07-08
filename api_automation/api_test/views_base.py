# from django import views
# from django.http import HttpResponse
# import json
# from api_test.models import Project

# class Projects(views):
#     def get(self, request):
#         '''
#         通过view 获取所有项目
#         '''
#         json_list = []
#         projects = Project.objects.all()
#         for project in projects:
#             dict_project = {}
#             dict_project["name"] = project.name
#             dict_project["version"] = project.version
#             json_list.append(dict_project)

        
#         return HttpResponse(json.dump(json_list), content_type="application/json")
        