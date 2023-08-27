
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string
from django.utils import timezone

class User(AbstractUser):
    is_vendor = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions')
    

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Trigger the signal only for new user instances
        if not self.pk:
            create_auth_token(sender=self.__class__, instance=self, created=True)
    

class CustomToken(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    key = models.CharField(max_length=40, primary_key=True)
    created = models.DateTimeField(default=timezone.now)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        token_key = get_random_string(length=40)
        CustomToken.objects.create(user=instance, key=token_key)