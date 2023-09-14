from django.db import models
from config.models import IDMixin, TimeStampMixin
from frame.validators import frame_id_validator


class UserFrame(IDMixin, TimeStampMixin):
    user_id = models.IntegerField(null=False, blank=False)
    frame_id = models.IntegerField(null=False, blank=False)

    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        db_table = "user_frame"


class Frame(TimeStampMixin):
    id = models.AutoField(primary_key=True, validators=[frame_id_validator])
    cam_id = models.IntegerField()
    VideoColor = models.JSONField()
    TimeSection = models.DateTimeField()
    ChannelNo = models.IntegerField()
    ConfigNo = models.IntegerField()

    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        db_table = "frame"
