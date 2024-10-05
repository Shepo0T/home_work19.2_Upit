from Catalog.models import Category
from config.settings import CACHE_ENABLE
from django.core.cache import cache



def get_category_from_cache():
    if not CACHE_ENABLE:
        return Category.objects.all()
    key = 'proudcts_list'
    category = cache.get(key)
    if category is not None:
        return category
    category = Category.objects.all()
    cache.set(key, category)
    return category