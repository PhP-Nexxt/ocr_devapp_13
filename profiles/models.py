from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Here we have letting title and adress.

    Attribute:
    user (OneToOneField): user of the profil
    favorite_city (str): name of favorite city
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        String representation for profil model

        Returns:
            str: username of user
        """
        return self.user.username
