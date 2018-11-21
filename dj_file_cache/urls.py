from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from upload import views
from cache1 import views as v

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('upload/', views.UploadView.as_view()),
                  path('index/', v.index),
                  path('index1/', v.index1),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 测试环境配置访问上传文件的路径
