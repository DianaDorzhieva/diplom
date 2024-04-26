from rest_framework import status
from rest_framework.test import APITestCase
from course.models import Course
from materials.models import Materials
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
        self.course = Course.objects.create(
            name='Test Course',
            text='Test text'
        )
        self.client.force_authenticate(user=self.user)

    def test_list_materials(self):
        """Тестирование вывода списка материалов"""
        responce = self.client.get('/materials/materials/')
        self.assertEquals(responce.status_code, status.HTTP_200_OK)

    def test_create_materials(self):
        """Тестирование создания материала"""
        data = {"name": "Test", "text": "text", "course": self.course}
        responce = self.client.post('/materials/materials/create/', data=data)
        self.assertEquals(responce.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Course.objects.all().exists())

    def test_update_materials(self):
        """Тестирование изменения материала """
        materials = Materials.objects.create(name="Test3", text='test', course=self.course)
        responce = self.client.patch(f'/materials/materials/update/{materials.id}/', {'name': 'change'})
        self.assertEquals(responce.status_code, status.HTTP_200_OK)

    def test_delete_materials(self):
        """Тестирование удаления материала """
        materials = Materials.objects.create(name="Test", text='test', course=self.course)
        responce = self.client.delete(f'/materials/materials/delete/{materials.id}/')
        self.assertEquals(responce.status_code, status.HTTP_204_NO_CONTENT)
