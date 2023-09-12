from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.sessions.base_session import AbstractBaseSession
from config.session import SessionStore
from django.db import models
from config.models import IDMixin, TimeStampMixin


class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str | None = None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.save(using=self._db)
        return user


class User(IDMixin, TimeStampMixin, AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        db_table = "user"


class UserSession(AbstractBaseSession):
    user_id = models.IntegerField(null=True, db_index=True)

    class Meta:
        db_table = "user_session"

    @classmethod
    def get_session_store_class(cls):
        return SessionStore
