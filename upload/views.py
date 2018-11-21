from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from upload.models import Shop, Img


class UploadView(View):
    def get(self, request):
        return render(request, 'upload.html')

    def post(self, request):
        # post 获取的字符串部分的信息
        desc = request.POST.get('desc')
        name = request.POST.get('name')
        # 获取文件部分的信息
        # img = request.FILES.get('img')
        shop = Shop(desc=desc, name=name)
        shop.save()
        # 多图片部分
        img_list = request.FILES.getlist('img')
        images = []
        for image in img_list:
            images.append(Img(img=image, shop=shop, type=1))
        #   批量保存
        Img.objects.bulk_create(images)

        # shop = Shop(desc=desc, name=name, img=img)
        # shop.save()
        return HttpResponse('上传成功')
