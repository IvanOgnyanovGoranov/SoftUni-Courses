import os
from datetime import date, timedelta

import django
from django.db.models import QuerySet, Avg
from psycopg2._psycopg import Int, Float

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Book, Artist, Song, Product, Review, DrivingLicense, Driver


# Create queries within functions


def show_all_authors_with_their_books() -> str:
    result = []

    authors = Author.objects.all()

    for author in authors:
        books = Book.objects.filter(author_id=author)

        if not books:
            continue

        titles = ', '.join(b.title for b in books)

        result.append(f'{author.name} has written - {titles}!')

    return '\n'.join(result)

def delete_all_authors_without_books() -> None:
    Author.objects.filter(book__isnull=True).delete()



def add_song_to_artist(artist_name: str, song_title: str) -> None:
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.add(song)


def get_songs_by_artist(artist_name: str) -> QuerySet[Song]:
    return Artist.objects.get(name=artist_name).songs.all().order_by('id')


def remove_song_from_artist(artist_name: str, song_title: str) -> None:
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.remove(song)


def calculate_average_rating_for_product_by_name(product_name: str) -> Float:
    product = Product.objects.get(name=product_name)
    reviews = product.reviews.all()

    return reviews.aggregate(Avg('rating'))['rating__avg']


def get_reviews_with_high_ratings(threshold: int) -> QuerySet[Review]:
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews() -> QuerySet[Product]:
    return Product.objects.filter(rating__isnull=True).order_by('-name')


def delete_products_without_reviews() -> None:
    get_products_with_no_reviews().delete()


def calculate_licenses_expiration_dates() -> str:
    licenses_exp_date = []

    all_licenses = DrivingLicense.objects.all().order_by('-license_number')

    for l in all_licenses:
        exp_date = l.issue_date + timedelta(days=365)

        licenses_exp_date.append(f"License with number: {l.license_number} expires on {exp_date}!")

    return '\n'.join(licenses_exp_date)


def get_drivers_with_expired_licenses(due_date: date) -> QuerySet[Driver]:
    expiration_date = due_date - timedelta(days=365)
    drivers_with_exp_licenses = Driver.objects.filter(license__issue_date__gt=expiration_date)

    return drivers_with_exp_licenses




drivers_with_expired_licenses = get_drivers_with_expired_licenses(date(2023, 1, 1))
for driver in drivers_with_expired_licenses:

    print(f"{driver.first_name} {driver.last_name} has to renew their driving license!")
