from django.urls import re_path, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.include_format_suffixes = False

router.register(r'gatheritem', GatherItemView, basename='gatheritem')

urlpatterns = format_suffix_patterns([
    re_path(r'^', include(router.urls)),
])
