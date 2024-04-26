from django.urls import path
from testing_info.apps import TestingInfoConfig
from testing_info.views import Testing_infoListAPIView, Answer_userCreateAPIView, Answer_userListAPIView

app_name = TestingInfoConfig.name

urlpatterns = [

    path('testing/', Testing_infoListAPIView.as_view(), name='testing'),
    path('answer/', Answer_userCreateAPIView.as_view(), name='answer'),
    path('answer/list/', Answer_userListAPIView.as_view(), name='answer_list'),

]
