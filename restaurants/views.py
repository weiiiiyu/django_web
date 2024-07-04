# 在你的應用程式中的 views.py 文件中定義視圖
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Restaurant

def your_model_list(request):
    # 獲取所有的 YourModelName 物件
    objects = Restaurant.objects.all()
    data = list(objects.values())  # 將查詢集轉換為列表

    return JsonResponse(data, safe=False)

def your_model_detail(request, pk):
    # 根據主鍵(pk)獲取特定的 YourModelName 物件
    object = get_object_or_404(Restaurant, pk=pk)
    data = {
        'id': object.id,
        'field1': object.field1,
        'field2': object.field2,
        # 添加其他欄位...
    }

    return JsonResponse(data)