from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from django.db.models.query import QuerySet
from loguru import logger

from config.permissions import UnauthenticatedPOST
from frame.serializers import FrameSerializer, FrameContributorSerializer
from frame.models import UserFrame, Frame
from .responses import CreateVideoFrame
from user.models import UserSession


class VideoFrameViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated | UnauthenticatedPOST]
    serializer_class = FrameSerializer

    def get_queryset(self) -> QuerySet:
        user_id = self.request.user.id

        return Frame.objects.filter(
            id__in=UserFrame.objects.filter(user_id=user_id)
        )
    
    def create(self, request):
        frame_serializer = FrameSerializer(data=request.data)
        contributors_serializer = FrameContributorSerializer(data=request.data)

        if not frame_serializer.is_valid() or not contributors_serializer.is_valid():
            logger.error({**frame_serializer.errors, **contributors_serializer.errors})
        
        user_sessions = (UserSession
            .objects
            .filter(user_id__in=contributors_serializer.validated_data['contributors'])
            .all())

        if len(user_sessions) == 0:
            return Response(
                {'message': CreateVideoFrame.SUCCESS.substitute(count=len(user_sessions))},
                status=status.HTTP_201_CREATED
            )

        frame = frame_serializer.save()

        UserFrame.objects.bulk_create(
            (UserFrame(user_id=session.user_id, frame_id=frame.id) for session in user_sessions)
        )

        return Response(
            {'message': CreateVideoFrame.SUCCESS.substitute(count=len(user_sessions))},
            status=status.HTTP_201_CREATED
        )
