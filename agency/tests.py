from django.test import TestCase
from django.contrib.auth.models import User
from agency.models import Topic, Newspaper, Redactor


class TopicModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Topic.objects.create(name='Test Topic')

    def test_name_label(self):
        topic = Topic.objects.get(id=1)
        field_label = topic._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        topic = Topic.objects.get(id=1)
        max_length = topic._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)

    def test_object_name_is_name(self):
        topic = Topic.objects.get(id=1)
        expected_object_name = f'{topic.name}'
        self.assertEquals(expected_object_name, str(topic))


class RedactorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Redactor.objects.create(username="Test", first_name='Test', last_name='User', years_of_experience=5)

    def test_first_name_label(self):
        redactor = Redactor.objects.get(id=1)
        field_label = redactor._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_years_of_experience_default_value(self):
        redactor = Redactor.objects.get(id=1)
        default_value = redactor._meta.get_field('years_of_experience').default
        self.assertEquals(default_value, 0)

    def test_object_name_is_username(self):
        redactor = Redactor.objects.get(id=1)
        expected_object_name = f'{redactor.username} {redactor.first_name}, {redactor.last_name}'
        self.assertEquals(expected_object_name, str(redactor))

