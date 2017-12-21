# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView
from home.forms import HomeForm
from django.shortcuts import render, redirect
from home.models import Post, Friend
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


class HomeView(TemplateView):
    template_name = 'home/home.html'

    
    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-created')
        ## users = User.objects.all() but inorder to remove the current username
        users = User.objects.exclude(id=request.user.id)
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()

        args = {
            'form': form, 'posts': posts, 'users':users, 'friends': friends,
            }
        return render(request, self.template_name, args)



    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            text = form.cleaned_data['post']
            ## to clean or remove the letters on the form after submitted
            form = HomeForm() ## This will remove it
            return redirect('home:home')
            ## to re-display the current page and and remove the text argument that will be posted

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)

@login_required
def change_friends(request, operation, pk):
    new_friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, new_friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, new_friend)
    return redirect('home:home')
