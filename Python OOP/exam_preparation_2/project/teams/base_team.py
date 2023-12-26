from abc import ABC, abstractmethod
from typing import List
from math import floor



class BaseTeam(ABC):

    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment: List[object] = []
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Team name cannot be empty!")
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value
    
    @property
    def advantage(self):
        return self.__advantage
    
    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        self.__budget = value

    @abstractmethod
    def win(self):
        ...

    def get_statistics(self):
        equipment_total_price = sum(item.price for item in self.equipment)
        avg_protection = floor(sum(item.protection for item in self.equipment) / len(self.equipment)
                               ) if self.equipment else 0

        statistics_str = f"Name: {self.name}\n" + \
                         f"Country: {self.country}\n" + \
                         f"Advantage: {self.advantage}\n" + \
                         f"Budget: {self.budget:.2f}EUR\n" + \
                         f"Wins: {self.wins}\n" + \
                         f"Total Equipment Price {equipment_total_price:.2f}\n" + \
                         f"Average protection: {avg_protection}"
        return statistics_str
