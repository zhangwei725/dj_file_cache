import datetime

from django.core.cache import cache
from django.shortcuts import render

# 视图缓存
from django.views.decorators.cache import cache_page


# 大数据
# 云计算
# 人工智能 + 爬虫 + web

# 热数据  变化的数据
#
@cache_page(timeout=10 * 60, key_prefix='view_index_')
def index(request):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render(request, 'cache.html', locals())

def index1(request):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render(request, 'cache.html', locals())
