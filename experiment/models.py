from django.db import models

# Create your models here.
class CustomerSubscriptionUser(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
