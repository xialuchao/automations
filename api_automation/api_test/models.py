# Create your models here.
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

## 更新model之后，使用命令，同步到数据库表结构
# python manage.py makemigrations 和 python manage.py migrate

HTTP_CHOICE = (
    ('HTTP', 'HTTP'),
    ('HTTPS', 'HTTPS')
)

REQUEST_TYPE_CHOICE = (
    ('POST', 'POST'),
    ('GET', 'GET'),
    ('PUT', 'PUT'),
    ('DELETE', 'DELETE')
)

REQUEST_PARAMETER_TYPE_CHOICE = (
    ('form-data', '表单(form-data)'),
    ('raw', '源数据(raw)'),
    ('Restful', 'Restful')
)

PARAMETER_TYPE_CHOICE = (
    ('text', 'text'),
    ('file', 'file')
)

HTTP_CODE_CHOICE = (
    ('200', '200'),
    ('404', '404'),
    ('400', '400'),
    ('502', '502'),
    ('500', '500'),
    ('302', '302'),
)

EXAMINE_TYPE_CHOICE = (
    ('no_check', '不校验'),
    ('only_check_status', '校验http状态'),
    ('json', 'JSON校验'),
    ('entirely_check', '完全校验'),
    ('Regular_check', '正则校验'),
)

UNIT_CHOICE = (
    ('m', '分'),
    ('h', '时'),
    ('d', '天'),
    ('w', '周'),
)

RESULT_CHOICE = (
    ('PASS', '成功'),
    ('FAIL', '失败'),
)


TASK_CHOICE = (
    ('circulation', '循环'),
    ('timing', '定时'),
)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# ==================扩展用户====================================
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户', related_name='user')
    phone = models.CharField(max_length=11, default='', blank=True, verbose_name='手机号')

    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return self.phone


class Project(models.Model):
    """
    项目表
    """
    ProjectType = (
        ('Web', 'Web'),
        ('App', 'App')
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='项目名称')
    version = models.CharField(max_length=50, verbose_name='版本')
    type = models.CharField(max_length=50, verbose_name='类型', choices=ProjectType)
    description = models.CharField(max_length=1024, blank=True, null=True, verbose_name='描述')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = '项目'



class GlobalHost(models.Model):
    """
    host域名
    """
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='项目')
    name = models.CharField(max_length=50, verbose_name='名称')
    host = models.CharField(max_length=1024, verbose_name='Host地址')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HOST'
        verbose_name_plural = 'HOST管理'


class ApiInfo(models.Model):
    """
    接口信息
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='接口名称')
    httpType = models.CharField(max_length=50, default='HTTP', verbose_name='http/https', choices=HTTP_CHOICE)
    requestType = models.CharField(max_length=50, verbose_name='请求方式', choices=REQUEST_TYPE_CHOICE)
    apiAddress = models.CharField(max_length=1024, verbose_name='接口地址')
    
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '接口'
        verbose_name_plural = '接口管理'


class ApiHead(models.Model):
    id = models.AutoField(primary_key=True)
    api = models.ForeignKey(ApiInfo, on_delete=models.CASCADE, verbose_name="所属接口", related_name='headers')
    name = models.CharField(max_length=1024, verbose_name="标签")
    value = models.CharField(max_length=1024, blank=True, null=True, verbose_name='内容')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '请求头'
        verbose_name_plural = '请求头管理'


class ApiParameter(models.Model):
    id = models.AutoField(primary_key=True)
    api = models.ForeignKey(ApiInfo, on_delete=models.CASCADE, verbose_name="所属接口", related_name='requestParameter')
    name = models.CharField(max_length=1024, verbose_name="参数名")
    _type = models.CharField(default="String", max_length=1024, verbose_name='参数类型', choices=(('Int', 'Int'), ('String', 'String')))
    value = models.CharField(max_length=1024, blank=True, null=True, verbose_name='参数值')
    required = models.BooleanField(default=True, verbose_name="是否必填")
    restrict = models.CharField(max_length=1024, blank=True, null=True, verbose_name="输入限制")
    description = models.CharField(max_length=1024, blank=True, null=True, verbose_name="描述")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '请求参数'
        verbose_name_plural = '请求参数管理'


class ApiResponse(models.Model):
    id = models.AutoField(primary_key=True)
    api = models.ForeignKey(ApiInfo, on_delete=models.CASCADE, verbose_name="所属接口", related_name='response')
    name = models.CharField(max_length=1024, verbose_name="参数名")
    _type = models.CharField(default="String", max_length=1024, verbose_name='参数类型', choices=(('Int', 'Int'), ('String', 'String')))
    value = models.CharField(max_length=1024, blank=True, null=True, verbose_name='参数值')
    required = models.BooleanField(default=True, verbose_name="是否必含")
    description = models.CharField(max_length=1024, blank=True, null=True, verbose_name="描述")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '返回参数'
        verbose_name_plural = '返回参数管理'
