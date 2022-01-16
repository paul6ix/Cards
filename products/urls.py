from .views import LatestCardList
from django.urls import path, include

urlpatterns = [
    path('latest', LatestCardList.as_view())
]
