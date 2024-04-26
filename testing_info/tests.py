from rest_framework import status
from rest_framework.test import APITestCase
from course.models import Course
from users.models import User, UserRole


class Testing_infoTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email="Diana@mail.ru",
            FIO="Diana",
            password="123",
            role=UserRole.MODERATOR,
            pk=2
        )
        self.course = Course.objects.create(
            name='Test Course',
            text='Test text'
        )
        self.client.force_authenticate(user=self.user)

    def test_list_testing_info(self):
        """Тестирование вывода списка вопросов"""
        responce = self.client.get('/testing/testing/')
        self.assertEquals(responce.status_code, status.HTTP_200_OK)

    def test_answer_user_list(self):
        """Тестирование вывода списка ответов"""
        responce = self.client.get('/testing/answer/list/')
        self.assertEquals(responce.status_code, status.HTTP_200_OK)
