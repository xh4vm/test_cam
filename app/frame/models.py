from django.db import models
from config.models import IDMixin, TimeStampMixin
from frame.validators import video_color_schema_validator, frame_id_validator, cam_id_validator, channel_validator, config_validator


class UserFrame(IDMixin, TimeStampMixin):
    user_id = models.IntegerField(null=False, blank=False)
    frame_id = models.IntegerField(null=False, blank=False)

    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        db_table = 'user_frame'


class Frame(TimeStampMixin):
    id = models.AutoField(primary_key=True, validators=[frame_id_validator])
    cam_id = models.IntegerField(validators=[cam_id_validator])
    VideoColor = models.JSONField(validators=[video_color_schema_validator])
    TimeSection = models.DateTimeField()
    ChannelNo = models.IntegerField(validators=[channel_validator])
    ConfigNo = models.IntegerField(validators=[config_validator])

    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        db_table = 'frame'
