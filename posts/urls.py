from django.urls import path

from . import views
from profiles.views import InfoPageView

urlpatterns = [
    path(route='', view=views.home_page_view, name='home'),
    path(route='explore/', view=views.ExploreView.as_view(), name='explore'),
    path(route='info/<str:username>/', view=InfoPageView.as_view(), name='info'),
    path(route='add_post/', view=views.AddPostView.as_view(), name='add_post'),
]
