from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from frame.serializers import FrameSerializer, FrameContributorSerializer
from frame.models import Frame, UserFrame
from user.models import User


class VideoFrameView(APIView):

    def put(self, request):
        frame_serializer = FrameSerializer(data=request.data)
        contributors_serializer = FrameContributorSerializer(data=request.data)

        if not frame_serializer.is_valid() or not contributors_serializer.is_valid():
            return
        
        users = User.objects.filter(id__in=contributors_serializer.validated_data['contributors'])

        return Response({'message': '1'}, status=status.HTTP_201_CREATED)

    def get(self, request):
        return Response({'message': '1'}, status=status.HTTP_200_OK)
