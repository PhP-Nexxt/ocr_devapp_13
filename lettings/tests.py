from django.test import TestCase

# reverse get url from the name in urls.py
from django.urls import reverse
from lettings.models import Letting


class LettingsTestCase(TestCase):
    # Link with fixtures file of the app - Allow to lunch tests
    fixtures = ["letting.json", "address.json"]

    def test_letting(self):
        self.assertEqual(Letting.objects.count(), 6)

    def test_lettings_views_index(self):
        # get url of lettings views
        url = reverse("lettings_index")
        # request get on url
        response = self.client.get(url)
        # check status code = 200
        self.assertEqual(response.status_code, 200)
        # check get template is the one used in views
        self.assertTemplateUsed(response, "lettings/index.html")
        # check if lettings list is present in response
        self.assertTrue("lettings_list" in response.context)
        # Balance beetween number of objects get vs objects in database
        self.assertTrue(len(response.context.get("lettings_list")), Letting.objects.count)

    def test_lettings_views_detail(self):
        # get last letting registered
        letting = Letting.objects.last()
        # check letting exist
        self.assertIsNotNone(letting)
        # create url detail with id of letting
        url = reverse("letting", kwargs={"letting_id": letting.id})
        # request get on url
        response = self.client.get(url)
        # check status code = 200
        self.assertEqual(response.status_code, 200)
        # check get template is the one used in views
        self.assertTemplateUsed(response, "lettings/letting.html")
