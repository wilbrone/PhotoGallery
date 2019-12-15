from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.

# Create your tests here.
class LocationTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.new_location = Location(loct = 'Nairobi')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_location,Location))

     # Testing Save Method
    def test_save_method(self):
        self.new_location.save()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)


class CategoryTestClass(TestCase):
    
    def setUp(self):
        # Creating a new editor and saving it
        self.new_category = Category(cat = 'Food')

        self.new_category.save_editor()



    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))



    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()       