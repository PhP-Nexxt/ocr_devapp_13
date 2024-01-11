from django.test import TestCase
from profiles.models import Profile
from django.urls import reverse


class ProfilesTestCase(TestCase):
    # Link with fixtures file of the app - Allow to lunch tests
    fixtures = ["user.json", "profile.json"]

    def test_profiles(self):
        self.assertEqual(Profile.objects.count(), 4)

    def test_profil_views_index(self):
        # get url of profile views
        url = reverse("profiles_index")
        # request get on url
        response = self.client.get(url)
        # check status code = 200
        self.assertEqual(response.status_code, 200)
        # check get template is the one used in views
        self.assertTemplateUsed(response, "profiles/index.html")
        # check if profile list is present in response
        self.assertTrue("profiles_list" in response.context)
        # Balance beetween number of objects get vs objects in database
        self.assertTrue(len(response.context.get("profiles_list")), Profile.objects.count)

    def test_profiles_views_detail(self):
        # get last profile registered
        profile = Profile.objects.last()
        # check profile exist
        self.assertIsNotNone(profile)
        # create url detail with username of the profile
        url = reverse("profile", kwargs={"username": profile.user.username})
        # request get on url
        response = self.client.get(url)
        # check status code = 200
        self.assertEqual(response.status_code, 200)
        # check get template is the one used in views
        self.assertTemplateUsed(response, "profiles/profile.html")
