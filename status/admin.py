# -*- encoding: utf-8 -*-
from django.contrib import admin
# Register your models here.
from status.models import *


# Register your models here.
@admin.register(CurrentUsers)
class CurrentUserAdmin(admin.ModelAdmin):
    list_display = []
    for i in CurrentUsers._meta.get_fields():
         list_display.append(i.name)

    add_form_template = False
    change_form_template = False
    list_filter = ('trusted_ip', 'trusted_port')  # 过滤器
    search_fields = ('trusted_port', 'trusted_ip')  # 搜索字段

    # date_hierarchy = 'go_time'    # 详细时间分层筛选　
    #def has_add_permission(self, request):
    #    return False;

    #def has_delete_permission(self, request):
    #    return False;
    ## for i in list(Clients._meta.get_fields()):
    #    #if i) == u'common_name' or i.lower(
    #    #) == u'common_name' or i == u'common_name':
    #    #    continue
    #    list_display.append(i.filed_name)

# Register your models here.
@admin.register(LogsReport)
class LogsReportAdmin(admin.ModelAdmin):
    list_display = []
    for i in LogsReport._meta.get_fields():
        list_display.append(i.name)
    add_form_template = False
    change_form_template = False
    list_filter = ('trusted_ip', 'trusted_port')  # 过滤器
    search_fields = ('trusted_port', 'trusted_ip')  # 搜索字段

    # date_hierarchy = 'go_time'    # 详细时间分层筛选　
    #def has_add_permission(self, request):
    #    return False;

    #def has_delete_permission(self, request):
    #    return False;
    # for i in list(Clients._meta.get_fields()):
    #    #if i) == u'common_name' or i.lower(
    #    #) == u'common_name' or i == u'common_name':
    #    #    continue
    #    list_display.append(i.filed_name)
# post_save 在某个Model保存之后调用, 对于每个唯一的dispatch_uid,接收器都只被信号调用一次
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
@receiver(post_save, sender=User, dispatch_uid="my_unique_identifier")
def my_handler(sender, instance, **kwargs):
    print("hello world")
