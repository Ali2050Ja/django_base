from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from accounts.models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from posts.models import NewPost
from django.contrib import messages

UserModel = get_user_model()


# class DashboardView(generic.ListView):
#     model = CustomUser
#     template_name = 'profiles/profile.html'
#     context_object_name = 'profile'

@login_required
def dashboard_view(request, username):
    user = CustomUser.objects.filter(username=username)
    posts = NewPost.objects.filter(user__username=username)
    return render(request, 'profiles/profile.html', context={'profile': user, 'posts': posts})


@login_required
def follow_view(request, user_id):
    target_user = get_object_or_404(UserModel, id=user_id)
    if request.user.Followings.filter(id=user_id).exists() and request.user.id != user_id:
        messages.error(request, f'you already followed {target_user.username}')
    else:
        request.user.Followings.add(target_user)
        messages.success(request, f'you are now following {target_user.username}')
    return redirect('/')


@login_required
def info_page_view(request, username):
    info_page = CustomUser.objects.filter(username=username)
    posts = NewPost.objects.filter(user__username=username)
    return render(request=request, template_name='profiles/info.html', context={'pages': info_page, 'username': username, 'posts': posts})

