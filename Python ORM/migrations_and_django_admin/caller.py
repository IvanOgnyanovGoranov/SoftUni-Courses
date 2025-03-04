import os
import django
from main_app.models import Shoe

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

# Create queries within functions

print(Shoe.objects.values_list('brand', flat=True).distinct())
