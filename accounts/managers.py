from django.contrib.auth.models import BaseUserManager
from django.db.models.query import QuerySet




class UserManager(BaseUserManager):
    
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(email=email,password=password,**extra_fields)
    
    
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(deleted_at__isnull=True)
    
    def all_items(self) -> QuerySet:
        return super().get_queryset()