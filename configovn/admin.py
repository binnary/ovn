from django.contrib import admin
# Register your models here.
from django.core.checks import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from configovn.models import *
from django import forms


class PersonForm(forms.ModelForm):
    myform = models.CharField(max_length=254, blank=True, verbose_name="MYFORM",
                              help_text="""选择绑定本机网络地址,默认监听所有网络地址""")
    class Meta:
        model = ConfigsInfo
        exclude=[]
        #fields = ['id', 'proto']


# Register your models here.
@admin.register(ConfigsInfo)
class ConfigNormalAdmin(admin.ModelAdmin):
    list_display = ["user"]
   # form = PersonForm
    for i in ConfigsInfo._meta.get_fields():
        if i.name == 'id' or i.name == "user":
            continue
        list_display.append(i.name)

    def pass_audit_str(self):
        from django.utils.html import format_html
        parameter_str = 'id={}&status={}'.format(str(self.id), str(self.user))
        color_code = ''
        btn_str = '<a class="btn btn-xs btn-danger" href="{}">' \
                  '<input name="通过审核"' \
                  'type="button" id="passButton" ' \
                  'title="passButton" value="通过审核">' \
                  '</a>'
        return format_html(btn_str, '/pass_audit/?{}'.format(parameter_str))

    pass_audit_str.short_description = '通过审核'
    list_display.append(pass_audit_str)

    save_as_continue = False
    save_as = False

    # 增加自定义按钮
    actions = ['make_copy', 'custom_button', 'message_test']

    #def get_list_filter(self, request):

    def custom_button(self, request, queryset):
        pass

    # def get_urls(self):
    #     urls = super(ConfigNormalAdmin, self).get_urls()
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
    #    return False

    #def has_delete_permission(self, request, obj=None):
    #    return False

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            album = form.save()

        super().save_model(request, obj, form, change)
    class Meta:
        save_as_continue = False

    # for i in list(Clients._meta.get_fields()):
    #    #if i) == u'common_name' or i.lower(
    #    #) == u'common_name' or i == u'common_name':
    #    #    continue
    #    list_display.append(i.filed_name)

# Register your models here.
@admin.register(ConfigsAdvanced)
class ConfigAdvancedAdmin(admin.ModelAdmin):
    list_display = []
    for i in ConfigsAdvanced._meta.get_fields():
        list_display.append(i.name)
    add_form_template = False
    change_form_template = False
    #def changelist_view(self, request, extra_content=None):
    #    from configovn.views import GroupsView
    #    return GroupsView(request)
    #def get_urls(self):
    #    from django.urls import path
    #    from functools import partial, reduce, update_wrapper
    #    def wrap(view):
    #        def wrapper(*args, **kwargs):
    #            return self.admin_site.admin_view(view)(*args, **kwargs)
    #        wrapper.model_admin = self
    #        return update_wrapper(wrapper, view)

    #    info = self.model._meta.app_label, self.model._meta.model_name

    #    urlpatterns = [
    #        path('1/change/', wrap(self.changelist_view), ),
    #    ]
    #    return urlpatterns

