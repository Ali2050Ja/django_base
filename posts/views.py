from django.shortcuts import render
from django.views import generic

from .models import NewPost


class HomePage(generic.TemplateView):
    template_name = 'posts/home.html'


class ExploreView(generic.ListView):
    model = NewPost
    template_name = 'posts/explore_view.html'
    context_object_name = 'explore'
