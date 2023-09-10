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