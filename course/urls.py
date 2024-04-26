from django.urls import path
from course.apps import CourseConfig
from course.views import CourseCreateAPIView, CourseListAPIView, CourseRetrieveAPIView, CourseUpdateAPIView, \
    CourseDestroyAPIView

app_name = CourseConfig.name

urlpatterns = [
    path('course/create/', CourseCreateAPIView.as_view(), name='course_create'),
    path('course/', CourseListAPIView.as_view(), name='course_list'),
    path('course/<int:pk>/', CourseRetrieveAPIView.as_view(), name='course_pk'),
    path('course/update/<int:pk>/', CourseUpdateAPIView.as_view(), name='course_update'),
    path('course/delete/<int:pk>/', CourseDestroyAPIView.as_view(), name='course_delete'),

]
