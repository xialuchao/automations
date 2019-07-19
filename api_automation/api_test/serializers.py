from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from api_test.models import Project, GlobalHost, ApiInfo, ApiHead, ApiParameter, ApiResponse


class TokenSerializer(serializers.ModelSerializer):
    """
    用户信息序列化
    """
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    phone = serializers.CharField(source="user.user.phone")
    email = serializers.CharField(source="user.email")
    date_joined = serializers.CharField(source="user.date_joined")

    class Meta:
        model = Token
        fields = ('first_name', 'last_name', 'phone', 'email', 'key', 'date_joined')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name')


class ProjectDeserializer(serializers.ModelSerializer):
    """
    项目信息反序列化
    """
    class Meta:
        model = Project
        fields = ('id', 'name', 'version', 'type', 'description')


class ProjectSerializer(serializers.ModelSerializer):
    """
    项目信息序列化
    """
    # apiCount = serializers.SerializerMethodField()
    # dynamicCount = serializers.SerializerMethodField()
    # memberCount = serializers.SerializerMethodField()
    # LastUpdateTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    # createTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    # user = serializers.CharField(source='user.first_name')  # 因为报错，所以注释，一直提示找不到first name

    class Meta:
        model = Project
        fields = ('id', 'name', 'version', 'type', 'description')

    # def get_apiCount(self, obj):
    #     return obj.api_project.all().count()

    # def get_dynamicCount(self, obj):
    #     return obj.dynamic_project.all().count()

    # def get_memberCount(self, obj):
    #     return obj.member_project.all().count()


class GlobalHostSerializer(serializers.ModelSerializer):
    """
    host信息序列化
    """

    class Meta:
        model = GlobalHost
        fields = ('id', 'project_id', 'name', 'host')


class ApiHeadSerializer(serializers.ModelSerializer):
    """
    接口请求头序列化
    """
    class Meta:
        model = ApiHead
        fields = ('id', 'api', 'name', 'value')


class ApiHeadDeserializer(serializers.ModelSerializer):
    """
    接口请求头反序列化
    """

    class Meta:
        model = ApiHead
        fields = ('id', 'api', 'name', 'value')


class ApiParameterSerializer(serializers.ModelSerializer):
    """
    接口请求参数序列化
    """

    class Meta:
        model = ApiParameter
        fields = ('id', 'api', 'name', 'value', '_type', 'required', 'restrict', 'description')


class ApiParameterDeserializer(serializers.ModelSerializer):
    """
    接口请求参数反序列化
    """

    class Meta:
        model = ApiParameter
        fields = ('id', 'api', 'name', 'value', '_type', 'required', 'restrict', 'description')


class ApiResponseSerializer(serializers.ModelSerializer):
    """
    接口返回参数序列化
    """

    class Meta:
        model = ApiResponse
        fields = ('id', 'api', 'name', 'value', '_type', 'required', 'description')


class ApiResponseDeserializer(serializers.ModelSerializer):
    """
    接口返回参数序列化
    """

    class Meta:
        model = ApiResponse
        fields = ('id', 'api', 'name', 'value', '_type', 'required', 'description')


class ApiInfoSerializer(serializers.ModelSerializer):
    """
    接口详细信息序列化
    """
    # lastUpdateTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    headers = ApiHeadSerializer(many=True, read_only=True)
    requestParameter = ApiParameterSerializer(many=True, read_only=True)
    response = ApiResponseSerializer(many=True, read_only=True)
    # requestParameterRaw = ApiParameterRawSerializer(many=False, read_only=True)
    userUpdate = serializers.CharField(source='userUpdate.first_name')

    class Meta:
        model = ApiInfo
        fields = ('id', 'name', 'httpType', 'requestType', 'apiAddress', 'headers',
                  'requestParameterType', 'requestParameter', 'status', 'response')


class ApiInfoDeserializer(serializers.ModelSerializer):
    """
    接口详细信息序列化
    """
    class Meta:
        model = ApiInfo
        # fields = ('id', 'project_id', 'name', 'httpType',
        #           'requestType', 'apiAddress', 'requestParameterType', 'status',
        #           'mockCode', 'data', 'lastUpdateTime', 'userUpdate', 'description')
        fields = ('id', 'name', 'httpType', 'requestType', 'apiAddress')


# class ApiInfoDocSerializer(serializers.ModelSerializer):
#     """
#     接口详细信息序列化
#     """
#     First = ApiInfoSerializer(many=True, read_only=True)

#     class Meta:
#         model = ApiGroupLevelFirst
#         fields = ('id', 'name', 'First')


class ApiInfoListSerializer(serializers.ModelSerializer):
    """
    接口信息序列化
    """
    lastUpdateTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    userUpdate = serializers.CharField(source='userUpdate.first_name')

    class Meta:
        model = ApiInfo
        fields = ('id', 'name', 'requestType', 'apiAddress', 'mockStatus', 'lastUpdateTime', 'userUpdate')
