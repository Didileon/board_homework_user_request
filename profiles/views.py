from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView

from .models import Profile


class ProfileDetail(PermissionRequiredMixin, DetailView):
    """Профиль пользователя"""
    permission_required = ('profiles.change_profile',)
    model = Profile
    context_object_name = "profile"
    template_name = "profiles/user-detail.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_user'] = Profile.objects.get(pk=self.kwargs.get('pk')).user
        return context


class VisitorDetail(DetailView):
    """Профиль пользователя для посетителя сайта"""
    model = Profile
    context_object_name = "profile"
    template_name = "profiles/visitor-detail.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['profile_user'] = Profile.objects.get(pk=self.kwargs.get('pk')).user
    #     return context

