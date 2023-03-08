from .models import *
from .serializers import *
# from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# class AnnoteViewSet(viewsets.ModelViewSet):
#     queryset = Annote.objects.all()
#     serializer_class = AnnoteSerializer
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticatedOrReadOnly]
    

class AnnoteListCreate(ListCreateAPIView):
    queryset = Annote.objects.all()
    serializer_class = AnnoteSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class AnnoteRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Annote.objects.all()
    serializer_class = AnnoteSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class ImageListCreate(ListCreateAPIView):
    queryset = Imagess.objects.all()
    serializer_class = ImagesSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class ImageRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Imagess.objects.all()
    serializer_class = ImagesSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]