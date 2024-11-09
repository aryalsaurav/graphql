import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from .managers import UserManager

# Create your models here.

class NonDeletedManager(models.Manager):
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(deleted_at__isnull=True)
        return queryset

    def all_items(self):
        return super().get_queryset()
    


class Timestamp(models.Model):
    
    """ 
    Abstract model for date time record
    """
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)
    deleted_at = models.DateTimeField(null=True,blank=True)

    objects = NonDeletedManager()
    class Meta:
        abstract =True
        
    def delete(self,hard=False):
        if hard:
            super().delete()
        else:
            self.deleted_at = timezone.now()
            super().save()

class GenderChoices(models.TextChoices):
    MALE = 'Male', 'Male'
    FEMALE = 'Female', 'Female'
    OTHERS = 'Others', 'Others'


class User(AbstractUser):
    
    email = models.EmailField(max_length=254,unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10,choices=GenderChoices.choices)
    username = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    phone_no = models.CharField(null=True,blank=True,max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)
    deleted_at = models.DateTimeField(null=True,blank=True)
    
    USERNAME_FIELD = "email"
    
    objects = UserManager()
    
    REQUIRED_FIELDS = []
    
    
    def __str__(self) -> str:
        return self.first_name + self.last_name
