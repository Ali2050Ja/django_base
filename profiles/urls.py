from django.urls import path

from . import views

urlpatterns = [
    path(route='<str:username>/', view=views.dashboard_view, name='dashboard'),
    path(route='follow/<int:user_id>/', view=views.follow_view, name='follow'),
]
