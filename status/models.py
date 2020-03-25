# -*- encoding: utf-8 -*-
from django.db import models


class CurrentUsers(models.Model):
    objects = models.Manager()
    #    (time.strftime('%Y.%m.%d %H-%m-%S-%s',time.localtime(time.time())))
    id = models.AutoField(primary_key=True)
    bytes_received = models.CharField(max_length=254, blank=True, verbose_name=u'接收字节')
    bytes_sent = models.CharField(max_length=254, blank=True, verbose_name=u'发送字节')
    trusted_ip = models.CharField(max_length=254, blank=True, verbose_name=u'实际IP')
    trusted_port = models.CharField(max_length=254, blank=True, verbose_name=u'实际端口')
    ifconfig_pool_remote_ip = models.CharField(max_length=254, blank=True, verbose_name=u'远端IP')
    ifconfig_pool_netmask = models.CharField(max_length=254, blank=True, verbose_name=u'远端掩码')
    common_name = models.CharField(max_length=254, blank=True, verbose_name=u'用户名')
    starting_time = models.CharField(max_length=254, blank=True, verbose_name=u'连接开始时间')
    end_time = models.CharField(max_length=254, blank=True, verbose_name=u'连接结束时间')
    protocol = models.CharField(max_length=254, blank=True, verbose_name=u'协议类型')
    online = models.CharField(max_length=254, blank=True, verbose_name=u'在线状态')
    local_port = models.CharField(max_length=254, blank=True, verbose_name=u'本地端口')

    def __str__(self):
        return u'CurrentConnUser'

    class Meta:
        db_table = "CurrentUsers"
        ordering = ('common_name',)
        verbose_name = verbose_name_plural = u'当前用户'

class LogsReport(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    #    (time.strftime('%Y.%m.%d %H-%m-%S-%s',time.localtime(time.time())))
    bytes_received = models.CharField(max_length=254, blank=True, verbose_name=u'接收字节')
    bytes_sent = models.CharField(max_length=254, blank=True, verbose_name=u'发送字节')
    trusted_ip = models.CharField(max_length=254, blank=True, verbose_name=u'实际IP')
    trusted_port = models.CharField(max_length=254, blank=True, verbose_name=u'实际端口')
    remote_ip = models.CharField(max_length=254, blank=True, verbose_name=u'远端IP')
    remote_netmask = models.CharField(max_length=254, blank=True, verbose_name=u'远端掩码')
    common_name = models.CharField(max_length=254, blank=True, verbose_name=u'用户名')
    starting_time = models.CharField(max_length=254, blank=True, verbose_name=u'连接开始时间')
    end_time = models.CharField(max_length=254, blank=True, verbose_name=u'连接结束时间')
    protocol = models.CharField(max_length=254, blank=True, verbose_name=u'协议类型')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Logs"
        ordering = ('common_name',)
        verbose_name = verbose_name_plural = u'日志报告'
