from django.db import models

class Car(models.Model):
    TRANSMISSION_CHOICES = [
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
    ]

    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    transmission = models.CharField(max_length=10, choices=TRANSMISSION_CHOICES, default='manual')
    main_image = models.ImageField(upload_to='cars/')

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

class CarImage(models.Model):
    car = models.ForeignKey(Car, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cars/gallery/')

    def __str__(self):
        return f"Image of {self.car}"
