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

#         self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
#         self.new_article.save()

#         self.new_article.tags.add(self.new_tag)

        # self.new_image= Image(title = 'BB', description ='Test Description', image ='/media/images/ilnur-kalimullin-kP1AxmCyEXM-unsplash2.jpg')
        
#     def test_get_news_today(self):
#         today_news = Article.todays_news()
#         self.assertTrue(len(today_news)>0)


    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()       