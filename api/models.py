from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_type = (
        (1, '学生'),
        (2, '教职工'),
    )
    healthy_type = (
        (1, '良好'),
        (2, '疑似'),
        (3, '确诊'),
    )
    touched_type = (
        (1, '无接触史'),
        (2, '目前仍然在湖北'),
        (3, '与确证患者有密切接触经历'),
        (4, '2020年1月10日后在湖北逗留过'),
    )
    userType = models.IntegerField(default=1, choices=user_type, verbose_name='用户类型')
    phoneNumber = models.CharField(default='', max_length=64, verbose_name='手机号')
    realName = models.CharField(default='', max_length=20, verbose_name='真实姓名')
    ifHealthy = models.IntegerField(default=1, choices=healthy_type, verbose_name='健康状态')
    ifTouched = models.IntegerField(default=1, choices=touched_type, verbose_name='接触史')

    class Meta:
        verbose_name = '用户信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class CheckRecord(models.Model):
    checkRecordPerson = models.ForeignKey(User, default=None, related_name='checkRecordPerson',
                                          on_delete=models.CASCADE, verbose_name='打卡人')
    temperature = models.DecimalField(default=None, max_digits=4, decimal_places=1, verbose_name='体温')
    location = models.CharField(default='', max_length=200, verbose_name='所在区域')
    checkRecordTime = models.DateTimeField(null=True, auto_now=True, verbose_name='打卡时间')

    class Meta:
        verbose_name = '打卡记录表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.checkRecordPerson


