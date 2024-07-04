from django.db import models

# Create your models here.

class YourModelName(models.Model):
    # 定義模型的欄位
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    # 其他欄位...

    def __str__(self):
        return self.field1  # 返回一個可讀的字符串表示

# 請記得在 settings.py 中設置 'YOUR_APP_NAME.apps.YourAppNameConfig' 以啟用應用程式