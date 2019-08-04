from django.contrib import admin

# Register your models here.
from .models import CustomerSubscriptionUser


class CustomerSubscritpionAd(admin.ModelAdmin):
    list_display = ('email', 'time_stamp')




admin.site.register(CustomerSubscriptionUser, CustomerSubscritpionAd)