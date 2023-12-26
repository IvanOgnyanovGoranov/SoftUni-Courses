from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    def __init__(self, name):
        super().__init__(name, oxygen_level=540)

    def miss(self, time_to_catch: int):
        oxygen_to_decrease = round(time_to_catch * 0.3)
        if self.oxygen_level - oxygen_to_decrease < 0:
            self.oxygen_level = 0
            return
        self.oxygen_level -= oxygen_to_decrease

    def renew_oxy(self):
        self.oxygen_level = 540
