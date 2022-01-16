from .views import LatestCardList
from django.urls import path, include

app_name = 'products'
urlpatterns = [
    path('latest/', LatestCardList.as_view(), name='latest'),
]
