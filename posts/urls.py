from django.urls import path

from . import views
from profiles.views import info_page_view as view

urlpatterns = [
    path(route='', view=views.HomePage.as_view(), name='home'),
    path(route='<str:username>/', view=view, name='info'),
    path(route='explore/', view=views.ExploreView.as_view(), name='explore'),
]