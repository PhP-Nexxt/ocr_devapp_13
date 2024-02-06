from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator

# Get data from oc_lettings_site


class Address(models.Model):
    """
    Here the model represente the adress of a 'letting'.
    A letting is a place available for rent.

    Attributes:
        number (int): number of the street
        street (str): street name
        city (str): city name
        state (str): state code
        zip_code (int): zip code
        country_iso_code (str): country iso code
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        """
        meta class for adress.
        Add singular or plural in select (pluralisation error).
        """

        verbose_name = "Adress"
        verbose_name_plural = "Adresses"

    def __str__(self):
        """
        String representation for adress model.

        Returns:
            str: number & street
        """
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """
    Here we have letting title ans adress.

    Attribute:
    title (str): title of the letting
    address (OneToOneField): adress of the letting
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        String representation for lettings model

        Returns:
            str: title
        """
        return self.title
