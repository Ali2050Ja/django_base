from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from .models import NewPost


# class HomePage(generic.TemplateView):
#     template_name = 'posts/home.html'

@login_required
def home_page_view(request):
    posts = NewPost.objects.filter(user__in=request.user.Followings.all())
    return render(request, 'posts/home.html', context={'posts': posts})


class ExploreView(generic.ListView):
    model = NewPost
    template_name = 'posts/explore_view.html'
    context_object_name = 'explore'


class AddPostView(generic.CreateView):
    model = NewPost
    fields = ['image', 'caption']
    template_name = 'posts/new_post.html'
    context_object_name = 'form'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        value = form.save(commit=False)
        value.user = self.request.user
        value.image = self.request.FILES('image')
        return super().form_valid(form)
