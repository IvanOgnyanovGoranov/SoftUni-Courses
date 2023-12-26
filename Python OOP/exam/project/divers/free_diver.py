from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    def __init__(self, name):
        super().__init__(name, oxygen_level=120)

    def miss(self, time_to_catch: int):
        oxygen_to_decrease = round(time_to_catch * 0.6)
        if self.oxygen_level - oxygen_to_decrease < 0:
            self.oxygen_level = 0
            return
        self.oxygen_level -= oxygen_to_decrease

    def renew_oxy(self):
        self.oxygen_level = 120

