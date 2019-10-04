from django.test import TestCase
from django.urls import reverse
from .models import File

class FileModelTestCase(TestCase):

    def test_speech2text(self):
        self.assertEqual(File.speech2text(), "hello transcriber output")
    
    def test_file_index_view(self):
        response = self.client.get(reverse('audio:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['file_list'], [])

