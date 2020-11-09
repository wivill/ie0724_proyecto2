# citas/testPosts.py

from django.test import TestCase
from citas.models import usuario

class PostTestCase(TestCase):
    def testPost(self):
        post = usuario(name="Nombre Apellido", gender="M", place="Nowhere", phone_number="8888-7777", age="26", allergies="Minoxidil")
        self.assertEqual(post.name, "Nombre Apellido")
        self.assertEqual(post.gender, "M")
        self.assertEqual(post.place, "Nowhere")
        self.assertEqual(post.phone_number, "8888-7777")
        self.assertEqual(post.age, "26")
        self.assertEqual(post.allergies, "Minoxidil")

