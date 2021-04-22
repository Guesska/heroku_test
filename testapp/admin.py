from django.contrib import admin
from .models import *
# Register your models here.


class AdminAboutMe(admin.ModelAdmin):
    list_display = ('image',)


admin.site.register(AboutMe, AdminAboutMe)
