import os
from typing import List

import django
from django.db.models import Case, When, Value

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import ArtworkGallery, Laptop, ChessPlayer


# Create and check models
def show_highest_rated_art() -> str:
    highest_rating = ArtworkGallery.objects.order_by('-rating').first()

    return f"{highest_rating.art_name} is the highest-rated art with a {highest_rating.rating} rating!"
# Run and print your queries


def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery):
    ArtworkGallery.objects.bulk_create([first_art, second_art])


def delete_negative_rated_arts():
     ArtworkGallery.objects.all().filter(rating__lt=0).delete()


def show_the_most_expensive_laptop() -> str:
    highest_price = Laptop.objects.order_by('-price').first()

    return f"{highest_price.brand} is the most expensive laptop available for {highest_price.price}$!"


def bulk_create_laptops(args: List[Laptop]) -> None:
    Laptop.objects.bulk_create(args)


def update_to_512_GB_storage() -> None:
    Laptop.objects.filter(brand__in=['Lenovo', 'Asus']).update(storage=512)


def update_to_16_GB_memory() -> None:
    Laptop.objects.filter(brand__in=["Apple", "Dell", "Acer"]).update(memory=16)


def update_operation_systems() -> None:
    Laptop.objects.update(
        operation_system=Case(
            When(brand='Asus', then=Value('Windows')),
            When(brand='Apple', then=Value('MacOS')),
            When(brand='Lenovo', then=Value('Chrome OS')),
            When(brand__in=('Dell', 'Acer'), then=Value('Apple')),
        )
    )


def delete_inexpensive_laptops():
    Laptop.objects.filter(price__lt=1200).delete()


def bulk_create_chess_players(args: List[ChessPlayer]):
    ChessPlayer.objects.bulk_create(args)


def delete_chess_players() -> None:
    ChessPlayer.objects.filter(title='no title').delete()


def change_chess_games_won():
    ChessPlayer.objects.filter(title='GM').update(games_won=30)


def change_chess_games_lost():
    ChessPlayer.objects.filter(title='no title').update(games_lost=25)


def change_chess_games_drawn():
    ChessPlayer.objects.all().update(games_drawn=10)


def grand_chess_title_GM():
    ChessPlayer.objects.filter(rating__gte=2400).update(title='GM')


def grand_chess_title_IM():
    ChessPlayer.objects.filter(rating__gte=2300, rating__lte=2399).update(title='IM')


def grand_chess_title_FM():
    ChessPlayer.objects.filter(rating__gte=2200, rating__lte=2299).update(title='FM')


def grand_chess_title_regular_player():
    ChessPlayer.objects.filter(rating__gte=0, rating__lte=2199).update(title='regular player')

