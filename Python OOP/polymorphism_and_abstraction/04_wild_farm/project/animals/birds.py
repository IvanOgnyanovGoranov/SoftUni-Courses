from project.animals.animal import Bird
from project.food import Food, Meat


class Owl(Bird):
    WEIGHT_GAINED_PER_PIECE = 0.25

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * self.WEIGHT_GAINED_PER_PIECE
        self.food_eaten += food.quantity


class Hen(Bird):
    WEIGHT_GAINED_PER_PIECE = 0.35

    def make_sound(self):
        return "Cluck"

    def feed(self, food: Food):
        self.weight += food.quantity * self.WEIGHT_GAINED_PER_PIECE
        self.food_eaten += food.quantity

