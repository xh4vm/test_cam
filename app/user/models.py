from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class IDMixin(models.Model):
    id = models.AutoField(primary_key=True)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str | None = None):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.save(using=self._db)
        return user


class User(IDMixin, TimeStampMixin, AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'user'
