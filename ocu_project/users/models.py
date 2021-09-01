from typing import Tuple
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from groups.models import Group

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_leader(self, email, password):
        user = self.create_user(email=email, password=password)
        user.leader = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.leader = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=256, unique=True)
    is_active = models.BooleanField(default=True)
    leader = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    @property
    def is_leader(self):
        return self.leader

    @property
    def is_admin(self):
        return self.admin

    objects = UserManager()


class Student(models.Model):
    university_id = models.PositiveIntegerField(unique=True, null=False)
    full_name = models.CharField(max_length=200, null=False, default="")
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
