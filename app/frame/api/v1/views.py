from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from django.db.models.query import QuerySet
from loguru import logger
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from config.permissions import UnauthenticatedPOST
from frame.serializers import FrameSerializer, FrameContributorSerializer
from frame.models import UserFrame, Frame
from .responses import CreateVideoFrame
from user.models import UserSession


class VideoFrameViewSet(
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, GenericViewSet
):
    permission_classes = [IsAuthenticated | UnauthenticatedPOST]
    serializer_class = FrameSerializer

    def get_queryset(self) -> QuerySet:
        user_id = self.request.user.id
        return Frame.objects.filter(id__in=UserFrame.objects.values_list('frame_id', flat=True).filter(user_id=user_id))

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "cam_id": openapi.Schema(
                    title="Camera ID",
                    type=openapi.TYPE_INTEGER,
                ),
                "VideoColor": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "Brightness": openapi.Schema(
                            title="Brightness video color",
                            type=openapi.TYPE_INTEGER,
                        ),
                        "Contrast": openapi.Schema(
                            title="Contrast video color",
                            type=openapi.TYPE_INTEGER,
                        ),
                        "Hue": openapi.Schema(
                            title="Hue video color",
                            type=openapi.TYPE_INTEGER,
                        ),
                        "Saturation": openapi.Schema(
                            title="Saturation video color",
                            type=openapi.TYPE_INTEGER,
                        ),
                    },
                ),
                "TimeSection": openapi.Schema(
                    title="TimeSection",
                    type=openapi.TYPE_STRING,
                ),
                "ChannelNo": openapi.Schema(
                    title="Channel number",
                    type=openapi.TYPE_INTEGER,
                ),
                "ConfigNo": openapi.Schema(
                    title="Config number",
                    type=openapi.TYPE_INTEGER,
                ),
                "contributors": openapi.Schema(
                    title="contributors",
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Items(type=openapi.TYPE_INTEGER),
                ),
            },
        )
    )
    def create(self, request):
        frame_serializer = self.get_serializer(data=request.data)
        contributors_serializer = FrameContributorSerializer(data=request.data)

        if not frame_serializer.is_valid() or not contributors_serializer.is_valid():
            logger.error({**frame_serializer.errors, **contributors_serializer.errors})

        user_sessions = UserSession.objects.filter(
            user_id__in=contributors_serializer.validated_data["contributors"]
        ).all()

        if len(user_sessions) == 0:
            return Response(
                {
                    "message": CreateVideoFrame.SUCCESS.substitute(
                        count=len(user_sessions)
                    )
                },
                status=status.HTTP_201_CREATED,
            )

        frame = frame_serializer.save()

        UserFrame.objects.bulk_create(
            (
                UserFrame(user_id=session.user_id, frame_id=frame.id)
                for session in user_sessions
            )
        )

        return Response(
            {"message": CreateVideoFrame.SUCCESS.substitute(count=len(user_sessions))},
            status=status.HTTP_201_CREATED,
        )
