from django.urls import path

from .views import customer_subscribe, customer_unsubscribe

urlpatterns = [
    path('subscribe/', customer_subscribe, name="customer_subscribe"),
    path('unsubscribe/', customer_unsubscribe, name="customer_unsubscribe")
]