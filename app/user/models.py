from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.sessions.models import Session
from django.db import models
from config.models import IDMixin, TimeStampMixin


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


class UserSession(Session):
    # you can also add custom field if required like this user column which can be the FK to the user table 
    user = models.ForeignKey('user', on_delete=models.CASCADE) 

    class Meta:
        app_label = "user"
        db_table = "user_session"
