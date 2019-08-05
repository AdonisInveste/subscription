from django.conf import settings
from django.contrib import messages
from django.shortcuts import render

from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template


""" Create views """
from .forms import CustomerSubscriptionForm
from .models import CustomerSubscriptionUser



def customer_subscribe(request):
    form = CustomerSubscriptionForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if CustomerSubscriptionUser.objects.filter(email=instance.email).exists():
            messages.warning(request, 'This email exists already')
        else:
            instance.save()
            messages.success(request, 'Great!')

            subject = "Thank you for joining our community"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            subscription_message = "Hi, LET'S DANCE. If you want to unsubscribe got to http://127.0.0.1:8000/experiment/unsubscribe/ "
            send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=subscription_message, fail_silently=False)    

    context = {'form': form, }
    template = "experiment/subscribe.html"


    return render(request, template, context)




def customer_unsubscribe(request):
    form = CustomerSubscriptionForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if CustomerSubscriptionUser.objects.filter(email=instance.email).exists():
            CustomerSubscriptionUser.objects.filter(email=instance.email).delete()
            messages.success(request, 'Sorry to see you go!')
        else:
           messages.warning(request, 'Email is not here!')

        subject = "You've been unsubscribed"
        from_email = settings.EMAIL_HOST_USER
        to_email = [instance.email]
        subscription_message = "BYE!"
        send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=subscription_message, fail_silently=False)
        print( send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=subscription_message, fail_silently=False))


    context = {'form': form, }
    template = "experiment/unsubscribe.html"


    return render(request, template, context)


