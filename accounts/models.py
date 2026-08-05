from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class Profile(models.Model):
    ROLE_PASSENGER = 'passenger'
    ROLE_STAFF = 'staff'
    ROLE_CHOICES = [
        (ROLE_PASSENGER, 'Passenger'),
        (ROLE_STAFF, 'AirportStaff')
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,
                                 related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES,default=ROLE_PASSENGER)

    
    def __str__(self):
        return f"{self.user.username}'s profile"
    @property
    def is_staff_role(self):
        return self.role == self.ROLE_STAFF
    
    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_or_update_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            
        else:
            Profile.objects.get_or_create(user=instance)
