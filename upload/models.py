from django.core.files.storage import FileSystemStorage
from django.db import models


# 图片+图片格式
class ImageFileStorage(FileSystemStorage):
    # /upload_to/img/IMG_20181120141250.jpeg

    def _save(self, name, content):
        import datetime
        import random
        import os
        old_name = name.split('/')[-1]
        # 图片的后缀名
        suffix_name = old_name.split('.')[-1]
        # IMG_20181120141250
        t = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        r = str(random.randint(100000, 999999))
        prefix_name = f"IMG_{t}{r}"
        image_path = os.path.dirname(name)
        name = os.path.join(image_path, f'{prefix_name}.{suffix_name}')
        return super()._save(name, content)


class Shop(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)

    # 框架自动配置了media
    # img = models.ImageField(upload_to='shop/%Y%m%d/')

    class Meta:
        db_table = 'shop'


class Img(models.Model):
    img = models.ImageField(upload_to='shop/img/', storage=ImageFileStorage(), max_length=255)
    # 1表示商品的图片
    # 2表示用户的图片
    type = models.SmallIntegerField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
