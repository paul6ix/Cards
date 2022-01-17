from .views import LatestCardList, CardDetail
from django.urls import path, include

app_name = 'products'
urlpatterns = [
    path('latest/', LatestCardList.as_view(), name='latest'),
    path('card/<slug:category_slug>/<slug:card_slug>/', CardDetail.as_view())
]
