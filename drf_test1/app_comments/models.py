from django.db import models


class Country(models.Model):
    """Model representing a country."""

    name = models.CharField(max_length=100)

    def __str__(self):
        """Returns the name of the country."""
        return self.name


class Manufacturer(models.Model):
    """Model representing a manufacturer."""

    name = models.CharField(max_length=100)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="manufacturers"
    )

    def __str__(self):
        """Returns the name of the manufacturer."""
        return self.name


class Car(models.Model):
    """Model representing a car."""

    name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        """Returns the name of the car."""
        return self.name


class Comment(models.Model):
    """Model representing a comment on a car."""

    email = models.EmailField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    def __str__(self):
        """Returns a string representation of the comment, including the email and the car name."""
        return f"{self.email} - {self.car.name}"
