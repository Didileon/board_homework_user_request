from . import views
from .models import Profile
from django.urls import path



urlpatterns = [
    path("<int:pk>/",  views.ProfileDetail.as_view(), name="profile-detail"),
    path("<int:pk>/", views.VisitorDetail.as_view(), name="visitor"),
    # path("<slug:slug>/",  views.ProfileDetail.as_view(), name="profile-detail"),

]