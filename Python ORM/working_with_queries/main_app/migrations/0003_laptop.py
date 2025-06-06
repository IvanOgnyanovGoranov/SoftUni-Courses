# Generated by Django 5.0.4 on 2025-04-02 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_artworkgallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('Asus', 'Asus'), ('Acer', 'Acer'), ('Apple', 'Apple'), ('Lenovo', 'Lenovo'), ('Dell', 'Dell')], max_length=20)),
                ('processor', models.CharField(max_length=100)),
                ('memory', models.PositiveIntegerField(help_text='Memory in GB')),
                ('storage', models.PositiveIntegerField(help_text='Storage in GB')),
                ('operation_system', models.CharField(choices=[('Windows', 'Windows'), ('MacOS', 'MacOS'), ('Linux', 'Linux'), ('Chrome OS', 'Chrome OS'), ('Safari', 'Safari')])),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
