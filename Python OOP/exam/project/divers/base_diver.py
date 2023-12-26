from abc import ABC, abstractmethod
from typing import List
from project.fish.base_fish import BaseFish


class BaseDiver(ABC):
    def __init__(self, name: str, oxygen_level: float):
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch: List = []
        self.competition_points = 0.0
        self.has_health_issue = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Diver name cannot be null or empty!")
        self.__name = value
    
    @property
    def oxygen_level(self):
        return self.__oxygen_level
    
    @oxygen_level.setter
    def oxygen_level(self, value):
        if value < 0:
            raise ValueError("Cannot create diver with negative oxygen level!")
        self.__oxygen_level = value

    @property
    def competition_points(self):
        return round(self.__competition_points, 1)

    @competition_points.setter
    def competition_points(self, value):
        self.__competition_points = value

    @abstractmethod
    def miss(self, time_to_catch: int):
        ...

    @abstractmethod
    def renew_oxy(self):
        ...

    def hit(self, fish: BaseFish):
        if self.__oxygen_level - fish.time_to_catch < 0:
            self.__oxygen_level = 0
            return
        self.__oxygen_level - fish.time_to_catch
        self.catch.append(fish)
        self.competition_points += round(fish.points, 1)

    def update_health_status(self):
        if not self.has_health_issue:
            self.has_health_issue = True
        else:
            self.has_health_issue = False

    def __str__(self):
        return f"{self.__class__.__name__}: [Name: {self.name}, Oxygen level left: {self.oxygen_level}, Fish caught: {len(self.catch)}, Points earned: {self.competition_points}] "

