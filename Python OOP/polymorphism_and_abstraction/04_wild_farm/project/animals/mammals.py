from project.animals.animal import Mammal
from project.food import Fruit, Vegetable, Meat


class Mouse(Mammal):
    WEIGHT_GAINED_PER_PIECE = 0.10

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if not isinstance(food, Vegetable) and not isinstance(food, Fruit):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * self.WEIGHT_GAINED_PER_PIECE
        self.food_eaten += food.quantity


class Dog(Mammal):
    WEIGHT_GAINED_PER_PIECE = 0.40

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * self.WEIGHT_GAINED_PER_PIECE
        self.food_eaten += food.quantity


class Cat(Mammal):
    WEIGHT_GAINED_PER_PIECE = 0.30

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if not isinstance(food, Vegetable) and not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * self.WEIGHT_GAINED_PER_PIECE
        self.food_eaten += food.quantity


class Tiger(Mammal):
    WEIGHT_GAINED_PER_PIECE = 1.00

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * self.WEIGHT_GAINED_PER_PIECE
        self.food_eaten += food.quantity
