from django.apps import AppConfig


class ConfigovnConfig(AppConfig):
    name = 'configovn'
    verbose_name = '服务配置'
    def ready(self):
        # importing model classes
        from .models import ConfigsInfo, ConfigsAdvanced
        ConfigsInfo = self.get_model('ConfigsInfo')
        ConfigsAdvanced = self.get_model('ConfigsAdvanced')

        for i in ConfigsInfo._meta.get_fields():
            print('reday==='+i.name)
        # registering signals with the model's string label
        #pre_save.connect(receiver, sender='app_label.MyModel')
