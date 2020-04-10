from django.contrib import admin
from django.contrib.auth.models import Group

#Unregister Group
admin.site.unregister(Group)

#Changing the title of Django Admin
admin.site.site_header = "Devnote Scrapy"

# Register your models here.
