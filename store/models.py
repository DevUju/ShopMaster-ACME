from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    stars = models.IntegerField(default=0)
    image = models.ImageField(upload_to='product_images/', null=False, blank=False)

    def __str__(self):
        return self.name


