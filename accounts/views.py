# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from accounts.forms import (
             RegisterationForm,
             EditProfileForm,
        )
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required  ## to give denial access if not authenticated/logged in

def register(request):
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = RegisterationForm()

        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)

## we use this decorators like this

## The pk parameter will be none if there is none but will be added if there is to differenciate view_profile and view_profile_with_pk
@login_required
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)

    else:
        user = request.user
    args = {'user': user}

    return render(request, 'accounts/profile.html', args)

##@login_required Started using instead middleware's
@login_required
def edit_profile(request):
    if request.method == 'POST':
        ## form = UserChangeForm(request.POST, instance=request.user)  // but use instead my own EditProfileForm
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

@login_required
def change_password(request):
    if request.method == 'POST':
        ## form = UserChangeForm(request.POST, instance=request.user)  // but use instead my own EditProfileForm
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')

        else:
            return redirect('/account/change-password')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)
