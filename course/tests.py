from rest_framework import status
from rest_framework.test import APITestCase
from course.models import Course
from users.models import User, UserRole


class CourseTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email="Diana@mail.ru",
            FIO="Diana",
            password="123",
            role=UserRole.MODERATOR,
            pk=2
        )
        self.client.force_authenticate(user=self.user)

    def test_list_course(self):
        """Тестирование вывода списка курсов"""
        responce = self.client.get('/course/')
        self.assertEquals(responce.status_code, status.HTTP_200_OK)

    def test_create_course(self):
        """Тестирование создания курса"""
        data = {"name": "Test", "text": "text"}
        responce = self.client.post('/course/create/', data=data)
        self.assertEquals(responce.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Course.objects.all().exists())

    def test_update_course(self):
        """Тестирование изменения курса """
        course = Course.objects.create(name="Test3", text='test')
        responce = self.client.patch(f'/course/update/{course.id}/', {'name': 'change'})
        self.assertEquals(responce.status_code, status.HTTP_200_OK)

    def test_delete_course(self):
        """Тестирование удаления курса """
        course = Course.objects.create(name="Test", text='test')
        responce = self.client.delete(f'/course/delete/{course.id}/')
        print(responce)
        self.assertEquals(responce.status_code, status.HTTP_204_NO_CONTENT)
