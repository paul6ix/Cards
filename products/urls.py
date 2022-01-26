from .views import LatestCardList, CardDetail
from django.urls import path, include


urlpatterns = [
    path('latest/', LatestCardList.as_view(), name='latest'),
    path('card/<slug:category>/<slug:card>/', CardDetail.as_view()),
]
