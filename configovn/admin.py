from django.contrib import admin

from django.contrib import admin
# Register your models here.
from django.core.checks import messages

from configovn.models import *


# Register your models here.
@admin.register(ConfigsInfo)
class ConfigNormalAdmin(admin.ModelAdmin):
    list_display = []
    for i in ConfigsInfo._meta.get_fields():
        list_display.append(i.name)

    add_form_template = False
    change_form_template = False
    #list_filter = ('trusted_ip', 'trusted_port')  # 过滤器
    # search_fields = ('trusted_port', 'trusted_ip')  # 搜索字段
    # 增加自定义按钮
    actions = ['make_copy', 'custom_button', 'message_test']

    def custom_button(self, request, queryset):
        pass

    # 显示的文本，与django admin一致
    custom_button.short_description = '测试按钮'
    # icon，参考element-ui icon与https://fontawesome.com
    custom_button.icon = 'fas fa-audio-description'

    # 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    custom_button.type = 'Switch'

    # 给按钮追加自定义的颜色
    custom_button.style = 'color:black;'

    def make_copy(self, request, queryset):
        pass

    make_copy.short_description = '复制员工'

    def message_test(self, request, queryset):
        messages.add_message(request, messages.SUCCESS, '操作成功123123123123')

        # 给按钮增加确认

    message_test.confirm = '你是否执意要点击这个按钮？'
    #def has_change_permission(self, request):
    #    return True

    # date_hierarchy = 'go_time'    # 详细时间分层筛选　
    #def has_add_permission(self, request):
    #    return True

    #def has_delete_permission(self, request):
    #    return True

    class Meta:
        permissions = [
            ('black_article', '拉黑文章的权限'),
        ]
    # for i in list(Clients._meta.get_fields()):
    #    #if i) == u'common_name' or i.lower(
    #    #) == u'common_name' or i == u'common_name':
    #    #    continue
    #    list_display.append(i.filed_name)

# Register your models here.
@admin.register(ConfigsAdvanced)
class ConfigAdvancedAdmin(admin.ModelAdmin):
    list_display = []
    for i in ConfigsInfo._meta.get_fields():
        list_display.append(i.name)
    add_form_template = False
    change_form_template = False
    #list_filter = ('trusted_ip', 'trusted_port')  # 过滤器
    #search_fields = ('trusted_port', 'trusted_ip')  # 搜索字段

