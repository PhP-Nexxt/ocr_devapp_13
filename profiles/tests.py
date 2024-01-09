from django.test import TestCase
from profiles.models import Profile

class ProfilesTestCase(TestCase):
    # Link with fixtures file of the app - Allow to lunch tests
    fixtures = ["user.json", "profile.json"]
    
    def test_profiles(self):
        self.assertEqual(Profile.objects.count(), 4)
