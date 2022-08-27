from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from accounts.models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from posts.forms import PostForm
from posts.models import NewPost
from accounts.forms import CustomUserChangeForm

UserModel = get_user_model()


# class DashboardView(generic.ListView):
#     model = CustomUser
#     template_name = 'profiles/profile.html'
#     context_object_name = 'profile'

@login_required
def dashboard_view(request):
    user = CustomUser.objects.filter(username=request.user)
    posts = NewPost.objects.filter(user__username=request.user)
    form = PostForm()
    if request.method == 'POST':
        info = PostForm(request.POST, request.FILES)
        image = request.FILES['image']
        caption = request.POST['caption']
        value = NewPost.objects.create(user=request.user, image=image, caption=caption)
        form = PostForm()
        return render(request, 'profiles/profile.html', context={'profile': user, 'posts': posts, 'form': form})
    else:
        return render(request, 'profiles/profile.html', context={'profile': user, 'posts': posts, 'form': form})


@login_required
def follow_view(request, user_id):
    target_user = get_object_or_404(UserModel, id=user_id)
    users = CustomUser.objects.filter(pk=user_id)
    if request.user.Followings.filter(id=user_id).exists():
        messages.error(request, f'you already followed {target_user.username}')
    else:
        request.user.Followings.add(target_user)
        messages.success(request, f'you are now following {target_user.username}')
    for item in users:
        return redirect(reverse('info', args=[item.username]))


@login_required
def unfollow_view(request, user_id):
    target_user = get_object_or_404(UserModel, id=user_id)
    users = CustomUser.objects.filter(pk=user_id)
    if request.user.Followings.filter(id=user_id).exists():
        request.user.Followings.remove(target_user)
        messages.success(request, f'you are now unfollowing {target_user.username}')
    else:
        messages.error(request, f'you already followed {target_user.username}')
    for item in users:
        return redirect(reverse('info', args=[item.username]))


# @login_required
# def info_page_view(request, username):
#     info_page = CustomUser.objects.filter(username=username)
#     posts = NewPost.objects.filter(user__username=username)
#     followed = request.user.Followings.filter(username=username).exists()
#     return render(request=request, template_name='profiles/info.html',
#                   context={'pages': info_page, 'username': username, 'posts': posts, 'followed': followed})


class InfoPageView(LoginRequiredMixin, generic.ListView):
    template_name = 'profiles/info.html'
    model = CustomUser

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(InfoPageView, self).get_context_data()
        context['pages'] = CustomUser.objects.filter(username=self.kwargs.get('username'))
        context['posts'] = NewPost.objects.filter(user__username=self.kwargs.get('username'))
        context['username'] = self.kwargs.get('username')
        context['followed'] = self.request.user.Followings.filter(username=self.kwargs.get('username')).exists()
        return context


class EditProfile(LoginRequiredMixin, generic.UpdateView):
    model = CustomUser
    fields = ['Image', 'username', 'Name', 'Website', 'Bio']
    template_name = 'profiles/edit_profile.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self):
        return self.request.user


class DeletePost(generic.DeleteView):
    model = NewPost
    template_name = 'profiles/delete_post.html'
    success_url = reverse_lazy('dashboard')
