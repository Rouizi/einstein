from django.test import TestCase
from django.urls import reverse

from core.models import Wihda, Exercise, School


class ExerciseWihdaTests(TestCase):
    def setUp(self):
        self.school1 = School.objects.create(school_year='school1')
        self.school2 = School.objects.create(school_year='school2')
        self.wihda1 = Wihda.objects.create(
            name='wihda1', school_id=self.school1.id)
        self.exercise1 = Exercise.objects.create(wihda=self.wihda1)

    def test_view_render_exercises(self):
        response = self.client.get(
            reverse('core:exercise_wihda'), {
                'wihda': self.wihda1.name, 'school_year_id': self.school1.id}
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/exercises_wihda.html')
        self.assertEqual(response.context['exercises'][0], self.exercise1)
        self.assertEqual(response.context['wihda'], self.wihda1)

    def test_view_returns_404_if_wihda_invalid(self):
        """The view return a 404 error if the wihda is not in the database"""
        response = self.client.get(
            reverse('core:exercise_wihda'), {
                'wihda': 'wihda2', 'school_year_id': self.school1.id}
        )
        self.assertEqual(response.status_code, 404)

    def test_view_returns_404_if_school_id_invalid(self):
        """The view return a 404 error if the school_id is not not related to the wihda"""
        response = self.client.get(
            reverse('core:exercise_wihda'), {
                'wihda': self.wihda1.name, 'school_year_id': self.school2.id}
        )
        self.assertEqual(response.status_code, 404)
