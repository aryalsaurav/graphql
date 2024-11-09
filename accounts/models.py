import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


from .managers import UserManager

# Create your models here.


class Timestamp(models.Model):
    
    """ 
    Abstract model for date time record
    """
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)
    deleted_at = models.DateTimeField(null=True,blank=True)

    
    class Meta:
        abstract =True


class GenderChoices(models.TextChoices):
    MALE = 'Male', 'Male'
    FEMALE = 'Female', 'Female'
    OTHERS = 'Others', 'Others'


class User(AbstractUser,Timestamp):
    
    email = models.EmailField(max_length=254,unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10,choices=GenderChoices.choices)
    username = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    phone_no = models.CharField(null=True,blank=True,max_length=10)
    
    USERNAME_FIELD = "email"
    
    objects = UserManager()
    
    REQUIRED_FIELDS = []
    
    
    def __str__(self) -> str:
        return self.first_name + self.last_name
