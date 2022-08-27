from django.urls import path

from . import views

urlpatterns = [
    path(route='', view=views.dashboard_view, name='dashboard'),
    path(route='follow/<int:user_id>/', view=views.follow_view, name='follow'),
    path(route='unfollow/<int:user_id>/', view=views.unfollow_view, name='unfollow'),
    path(route='edit/', view=views.EditProfile.as_view(), name='edit'),
    path(route='delete/<int:pk>/', view=views.DeletePost.as_view(), name='delete'),
]
