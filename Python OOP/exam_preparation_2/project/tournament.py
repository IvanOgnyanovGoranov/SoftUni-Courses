from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.outdoor_team import OutdoorTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.base_team import BaseTeam


class Tournament:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type):
        if equipment_type != "KneePad" and equipment_type != "ElbowPad":
            raise Exception("Invalid equipment type!")
        if equipment_type == "KneePad":
            self.equipment.append(KneePad)
            return f"{equipment_type} was successfully added."
        elif equipment_type == "ElbowPad":
            self.equipment.append(ElbowPad)
            return f"{equipment_type} was successfully added."

    def add_team(self, team_type, team_name, country, advantage: int):
        if team_type != "OutdoorTeam" and team_type != "IndoorTeam":
            raise Exception("Invalid team type!")
        if len(self.teams) == self.capacity:
            return "Not enough tournament capacity."

        if team_type == "OutdoorTeam":
            self.teams.append(OutdoorTeam(team_name, country, advantage))
            return f"{team_type} was successfully added."
        if team_type == "IndoorTeam":
            self.teams.append(IndoorTeam(team_name, country, advantage))
            return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        current_team = self.team_finder(team_name)

        if current_team is not None:
            if current_team.budget < self.equipment_price_finder(equipment_type):
                raise Exception("Budget is not enough!")
        if current_team is not None:
            for i in range(len(self.equipment)-1, -1, -1):
                equipment = self.equipment[i]
                if equipment_type == equipment.__class__.__name__:
                    current_team.equipment.append(equipment)
                    self.equipment.remove(equipment)
                    current_team.budget -= self.equipment_price_finder(equipment_type)
                    return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        current_team = self.team_finder(team_name)
        if current_team is None:
            raise Exception("No such team!")
        if current_team.wins > 0:
            raise Exception(f"The team has {current_team.wins} wins! Removal is impossible!")
        self.teams.remove(current_team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        num_of_changed_equipment = 0
        for equipment in self.equipment:
            if equipment_type == equipment.__class__.__name__:
                equipment.increase_price()
                num_of_changed_equipment += 1
        return f"Successfully changed {num_of_changed_equipment}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team_1 = self.team_finder(team_name1)
        team_2 = self.team_finder(team_name2)

        if team_1.__class__.__name__ != team_2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        team_1_total_points = team_1.advantage
        team_2_total_points = team_2.advantage

        for equipment in team_1.equipment:
            team_1_total_points += equipment.protection

        for equipment in team_2.equipment:
            team_2_total_points += equipment.protection

        if team_1_total_points > team_2_total_points:
            team_1.win()
            return f"The winner is {team_name1}"
        elif team_1_total_points < team_2_total_points:
            team_2.win()
            return f"The winner is {team_name2}"
        else:
            return "No winner in this game."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda x: x.wins, reverse=True)
        for team in sorted_teams:
            print(team.get_statistics())

    def team_finder(self, team_name):
        for team in self.teams:
            if team.name == team_name:
                return team
        return None

    def equipment_price_finder(self, equipment_type):
        if equipment_type == "KneePad":
            return KneePad().price
        if equipment_type == "ElbowPad":
            return ElbowPad().price





