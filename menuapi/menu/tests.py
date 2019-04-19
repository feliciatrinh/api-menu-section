from django.test import TestCase

from .models import MenuSection
from .serializers import MenuSectionSerializer

class MenuSectionTest(TestCase): 
	def createSection(self, name="test section"): 
		return MenuSection.objects.create(name=name)

	def test_create(self): 
		section = self.createSection()
		self.assertTrue(isinstance(section, MenuSection))
		self.assertEqual(section.name, "test section")
