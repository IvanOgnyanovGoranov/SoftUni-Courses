import os
import django
from django.db.models import QuerySet

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car, Task


# Create queries within functions
def create_pet(name: str, species: str) -> str:
    pet = Pet.objects.create(name=name, species=species,)

    return f"{pet.name} is a very cute {pet.species}!"


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool) -> str:
    artifact = Artifact.objects.create(name=name,
                                       origin=origin,
                                       age=age,
                                       description=description,
                                       is_magical=is_magical)

    return f'The artifact {artifact.name} is {artifact.age} years old!'

def rename_artifact(artifact: Artifact, new_name: str):
    if artifact.is_magical and artifact.age > 250:
        artifact.name = new_name
        artifact.save()


def delete_all_artifacts():
    Artifact.objects.all().delete()


# def create_three_locations():
#     base_name = 'name'
#     base_region = 'region'
#     base_population = 1000
#     base_description = 'Somewhere nice'
#     is_capital = False
#
#     for i in range(3):
#         Location.objects.create(
#             name=f"{base_name}{i}",
#             region=f"{base_region}{i}",
#             population=base_population + i,
#             description=f"{base_description}{i}",
#             is_capital=is_capital
#         )


def show_all_locations():
    locations = Location.objects.all().order_by('-id')

    return '\n'.join(f'{l.name} has a population of {l.population}!' for l in locations)


def new_capital():
    first_location = Location.objects.first()
    first_location.is_capital = True
    first_location.save()


def get_capitals():
    return Location.objects.filter(is_capital=True).values('name')


def delete_first_location():
    Location.objects.first().delete()


def apply_discount():
    cars = Car.objects.all()

    for car in cars:
        percentage = sum(int(digit) for digit in str(car.year)) / 100
        discount = float(car.price) * percentage
        car.price_with_discount = float(car.price) - discount
        car.save()


def get_recent_cars() -> QuerySet:
    return Car.objects.filter(year__gt=2020).values('model', 'price_with_discount')


def delete_last_car():
    Car.objects.last().delete()


def show_unfinished_tasks():
    unfinished_tasks = Task.objects.filter(is_finished=False)

    return '\n'.join(f'Task - {task.title} needs to be done until {task.due_date}!' for task in unfinished_tasks)


def complete_odd_tasks():
    odd_tasks = [t for t in Task.objects.all() if t.id % 2 != 0]

    for odd_task in odd_tasks:
        odd_task.is_finished = True
        odd_task.save()

    # Better solution
    # Task.objects.filter(id__mod=2=1).update(is_finished=True)


def encode_and_replace(text: str, task_title: str) -> None:
    decoded_text = ''.join(chr(ord(symbol) - 3)for symbol in text)
    Task.objects.filter(title=task_title).update(description=decoded_text)

    # tasks_with_matching_title = Task.objects.filter(title=task_title)
    #
    # for task in tasks_with_matching_title:
    #     task.description = decoded_text
    #
    # Task.objects.bulk_update(tasks_with_matching_title, ['description'])







