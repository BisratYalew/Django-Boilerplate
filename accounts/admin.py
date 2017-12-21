# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from accounts.models import UserProfile
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info', 'city', 'phone', 'website')

    def user_info(self, obj):
        return obj.description


    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('phone', 'user')
        ## queryset = queryset.order_by(-phone) to order it in descending order or reverse order, we will add second
        ## argument to sort by another value if the value is 0 or empty on the first argument value
        return queryset

    user_info.short_description = 'Info'


admin.site.register(UserProfile, UserProfileAdmin)


## to change the django-admin branding name -- admin.site.site_header = 'Administration'
