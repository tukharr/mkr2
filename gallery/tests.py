from django.test import TestCase

from django.test import TestCase
from .models import Image, Category
from django.utils import timezone
from django.urls import reverse

# class ModelCourseTests(TestCase):
#
#     def setUp(self) -> None:
#         Course.objects.create(
#             name='Test Course 1',
#             description='Test Course 1 description',
#             start_date=timezone.now().date(),
#             end_date=timezone.now().date() + timezone.timedelta(days=90)
#         )
#         Course.objects.create(
#             name='Test Course 2',
#             description='Test Course 2 description',
#             start_date=timezone.now().date() + timezone.timedelta(days=7),
#             end_date=timezone.now().date() + timezone.timedelta(days=14)
#         )
#         Course.objects.create(
#             name='Test Course 3',
#             description='Test Course 3 description',
#             start_date=timezone.now().date() - timezone.timedelta(days=7),
#             end_date=timezone.now().date() + timezone.timedelta(days=17)
#         )
#
#     def test_is_current_with_future_start_date(self):
#         course = Course.objects.get(name='Test Course 1')
#         self.assertTrue(course.is_current())
#
#     def test_is_current_with_future_end_date(self):
#         course = Course.objects.get(name='Test Course 2')
#         self.assertFalse(course.is_current())
#
#     def test_is_current_with_past_start_date(self):
#         course = Course.objects.get(name='Test Course 3')
#         self.assertTrue(course.is_current())


class ResponseTests(TestCase):

    def test_no_categories(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['categories'], [])

    def test_save_category(self):
        test_category = Category(name='Test Category')
        test_category.save()
        response = self.client.get(reverse('main'))
        self.assertQuerysetEqual(
            response.context['categories'],
            [test_category]
        )

    def test_delete_category(self):
        test_category = Category(name='Test Category')
        test_category.save()
        response = self.client.get(reverse('main'))
        self.assertQuerysetEqual(
            response.context['categories'],
            [test_category]
        )
        test_category.delete()
        response = self.client.get(reverse('main'))
        self.assertQuerysetEqual(
            response.context['categories'],
            []
        )

