import os
import django
from django.db.models import QuerySet

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Book, Artist, Song


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


songs = get_songs_by_artist("Daniel Di Angelo")