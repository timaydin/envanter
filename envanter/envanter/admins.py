from django.contrib import admin
from .models import Category, Component, Manufacturer, W, Ohm, DocumentType, Document, Datasheet, Package, LocationType, Location, Supplier, Purchase, ComponentDocumentLink, PurchaseDetail, PictureURL 


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ('model', 'manufacturer', 'category', 'stock')

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(W)
class WAdmin(admin.ModelAdmin):
    list_display = ('value',)

@admin.register(Ohm)
class OhmAdmin(admin.ModelAdmin):
    list_display = ('value',)

@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'document_type')

@admin.register(Datasheet)
class DatasheetAdmin(admin.ModelAdmin):
    list_display = ('title', 'document')

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(LocationType)
class LocationTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location_type')

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'date')

@admin.register(ComponentDocumentLink)
class ComponentDocumentLinkAdmin(admin.ModelAdmin):
    list_display = ('component', 'document')

@admin.register(PurchaseDetail)
class PurchaseDetailAdmin(admin.ModelAdmin):
    list_display = ('purchase', 'component', 'quantity')

@admin.register(PictureURL)
class PictureURLAdmin(admin.ModelAdmin):
    list_display = ('component', 'url')
    