from typing import List
from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Animal] = []

    def add_animal(self, animal, price) -> str:
        if len(self.animals) < self.__animal_capacity and price <= self.__budget:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif len(self.animals) < self.__animal_capacity and price > self.__budget:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_of_salaries = sum([w.salary for w in self.workers])
        if self.__budget >= sum_of_salaries:
            self.__budget -= sum_of_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        budget = sum([w.money_for_care for w in self.animals])
        if self.__budget >= budget:
            self.__budget -= budget
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        result = [f"You have {len(self.animals)} animals"]
        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]

        result.append(f"----- {len(lions)} Lions:")
        for l in lions:
            result.append(f"{l}")

        result.append(f"----- {len(tigers)} Tigers:")
        for l in tigers:
            result.append(f"{l}")

        result.append(f"----- {len(cheetahs)} Cheetahs:")
        for l in cheetahs:
            result.append(f"{l}")

        return "\n".join(result)

    def workers_status(self):
        result = [f"You have {len(self.workers)} workers"]

        keepers = [w for w in self.workers if w.__class__.__name__ == "Keeper"]
        caretakers = [w for w in self.workers if w.__class__.__name__ == "Caretaker"]
        vets = [w for w in self.workers if w.__class__.__name__ == "Vet"]

        result.append(f"----- {len(keepers)} Keepers:")
        for w in keepers:
            result.append(f"{w}")

        result.append(f"----- {len(caretakers)} Caretakers:")
        for w in caretakers:
            result.append(f"{w}")

        result.append(f"----- {len(vets)} Vets:")
        for w in vets:
            result.append(f"{w}")

        return "\n".join(result)
