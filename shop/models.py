from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name

class Items(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="pictures/")
    price = models.FloatField()
    sale = models.IntegerField()
    stock_amount = models.IntegerField()
    description = models.CharField(max_length=150, blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    def get_new_price(self):
        if self.sale > 0:
            return self.price - self.price * self.sale / 100