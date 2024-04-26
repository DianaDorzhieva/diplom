from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from testing_info.models import Testing_info, Answer_user
from testing_info.serliazers import Testing_infoSerializer, Answer_userSerializer
from rest_framework.response import Response


class Testing_infoListAPIView(generics.ListAPIView):
    serializer_class = Testing_infoSerializer
    queryset = Testing_info.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('materials_id',)


class Answer_userCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Answer_userSerializer
    queryset = Answer_user.objects.all()

    def post(self, request):
        test_id = self.request.data.get('test')
        test_item = get_object_or_404(Testing_info, id=test_id)
        user = self.request.user
        answer_item = self.request.data.get('answer')
        Answer_user.objects.create(answer=answer_item, test=test_item, user=user)

        if test_item.answer == answer_item:
            message = True
        else:
            message = False

        return Response({"message": message})


class Answer_userListAPIView(generics.ListAPIView):
    serializer_class = Answer_userSerializer
    queryset = Answer_user.objects.all()
    permission_classes = [IsAuthenticated]
