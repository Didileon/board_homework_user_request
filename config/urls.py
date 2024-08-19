from django.urls import path

from . import views
from .views import *


urlpatterns = [
    path('', AdvertList.as_view(), name="advert-list"),
    path('<int:pk>', AdvertDetail.as_view(), name="advert-detail"),
    path('create/', AdvertCreate.as_view(), name='advert_create'),
    path('<int:pk>/update/', AdvertUpdate.as_view(), name='advert_update'),
    path('<int:pk>/delete/', AdvertDelete.as_view(), name='advert_delete'),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    path('subscriptions/', subscriptions, name='subscriptions'),
    path("review_update/<int:pk>/", status_review_update, name="review_update"),
    path("review_delete/<int:pk>/", status_review_delete, name="review_delete"),
]