from rest_framework import generics
from materials.models import Materials
from materials.paginators import MaterialsPaginator
from materials.serliazers import MaterialsSerializer
from rest_framework.permissions import IsAuthenticated
from users.permission import IsModerator


class MaterialsCreateAPIView(generics.CreateAPIView):
    serializer_class = MaterialsSerializer
    permission_classes = [IsAuthenticated, IsModerator]


class MaterialsListAPIView(generics.ListAPIView):
    serializer_class = MaterialsSerializer
    queryset = Materials.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = MaterialsPaginator


class MaterialsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = MaterialsSerializer
    queryset = Materials.objects.all()
    permission_classes = [IsAuthenticated]


class MaterialsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = MaterialsSerializer
    queryset = Materials.objects.all()
    permission_classes = [IsAuthenticated, IsModerator]


class MaterialsDestroyAPIView(generics.DestroyAPIView):
    serializer_class = MaterialsSerializer
    queryset = Materials.objects.all()
    permission_classes = [IsAuthenticated, IsModerator]
