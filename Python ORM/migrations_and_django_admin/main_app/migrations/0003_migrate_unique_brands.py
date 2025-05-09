# Generated by Django 5.0.4 on 2025-02-20 05:18

from django.db import migrations

def create_unique_brands(apps, schema_editor):
    shoe = apps.get_model('main_app', 'Shoe')
    unique_brands = apps.get_model('main_app', 'UniqueBrand')

    unique_brand_names = shoe.objects.values_list('brand', flat=True).distinct()

    unique_brands.objects.bulk_create([unique_brands(brand=brand) for brand in unique_brand_names])
    # for brand_name in unique_brand_names:
    #     unique_brands.create(brand_name=brand_name)

def reverse_unique_brands(apps, schema_editor):
    unique_brands = apps.get_model('main_app', 'UniqueBrand')
    unique_brands.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_uniquebrand'),
    ]

    operations = [
        migrations.RunPython(create_unique_brands, reverse_unique_brands)
    ]
