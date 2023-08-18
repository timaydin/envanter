from django.db import models
import os 
from datetime import datetime

class W(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Ohm(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name

class DocumentType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Document(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True, blank=True)
    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    document_path = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Package(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class LocationType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location_type = models.ForeignKey(LocationType, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Purchase(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Purchase #{self.id}"

class Component(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    stock = models.IntegerField(default=0)
    
    def __str__(self):
        return self.model

class ComponentDocumentLink(models.Model):
    id = models.AutoField(primary_key=True)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Link #{self.id}"

class PurchaseDetail(models.Model):
    id = models.AutoField(primary_key=True)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return f"Purchase Detail #{self.id}"
    
class Datasheet(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return f"Data Sheet #{self.id}"
    
class PictureURL(models.Model):
    id = models.AutoField(primary_key=True)
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    url = models.CharField(max_length=500)
    
    def __str__(self):
        return f"Picture URL #{self.id}"
    
