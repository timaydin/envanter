from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Component(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    parca_no = models.CharField(max_length=100)
    uretici = models.CharField(max_length=100)
    birim_fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    stok_miktar = models.IntegerField()
    location_type = models.CharField(max_length=100)
    Ohm = models.DecimalField(max_digits=10, decimal_places=2)
    W = models.DecimalField(max_digits=10, decimal_places=2)
    teknik_ozellikler = models.TextField()
    foto = models.URLField(max_length=500, blank=True)
    dokuman = models.URLField(max_length=500, blank=True)

    def __str__(self):
        return self.model
