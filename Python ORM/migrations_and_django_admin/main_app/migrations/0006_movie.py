# Generated by Django 5.0.4 on 2025-02-26 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_uniquebrand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('release_year', models.PositiveIntegerField()),
                ('genre', models.CharField(max_length=50)),
            ],
        ),
    ]
