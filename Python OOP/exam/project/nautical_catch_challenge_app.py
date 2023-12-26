from typing import List
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.predatory_fish import PredatoryFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.divers.base_diver import BaseDiver


class NauticalCatchChallengeApp():
    VALID_DIVER_TYPES = {"ScubaDiver": ScubaDiver, "FreeDiver": FreeDiver}
    VALID_FISH_TYPES = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseDiver] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.VALID_DIVER_TYPES:
            return f"{diver_type} is not allowed in our competition."
        for diver in self.divers:
            if diver.name == diver_name:
                return f"{diver_name} is already a participant."

        diver = self.VALID_DIVER_TYPES[diver_type](diver_name)
        self.divers.append(diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."
        for fish in self.fish_list:
            if fish.name == fish_name:
                return f"{fish_name} is already permitted."

        fish = self.VALID_FISH_TYPES[fish_type](fish_name, points)
        self.fish_list.append(fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver_found = next((d for d in self.divers if d.name == diver_name), None)
        fish_found = [f for f in self.fish_list if diver_name == f.name]


        if diver_found is None:
            return f"{diver_name} is not registered for the competition."

        if not fish_found:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver_found.has_health_issue == True:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver_found.oxygen_level < fish_found.time_to_catch:
            return f"{diver_name} missed a good {fish_name}."

        if diver_found.oxygen_level == fish_found.time_to_catch:
            if is_lucky:
                diver_found.hit(fish_found)
                diver_found.has_health_issue = True
                return f"{diver_name} hits a {fish_found.points}pt. {fish_name}."
            else:
                diver_found.miss(fish_found.time_to_catch)
                return f"{diver_name} missed a good {fish_name}."

        if diver_found.oxygen_level > fish_found.time_to_catch:
            diver_found.hit(fish_found)
            return f"{diver_name} hits a {fish_found.points}pt. {fish_name}."

    def health_recovery(self):
        divers_recovered = 0
        for diver in self.divers:
            if diver.has_health_issue:
                diver.has_health_issue = False
                if diver.__class__.__name__ == "ScubaDiver":
                    diver.oxygen_level = 540
                else:
                    diver.oxygen_level = 120
                divers_recovered += 1
                return f"Divers recovered: {divers_recovered}"

    def diver_catch_report(self, diver_name: str):
        list_ = ["**{diver_name} Catch Report**"]
        diver = [d for d in self.divers if diver_name == d.name][0]

        for fish in diver.catch:
            list_.append(fish.fish_details)

        return "\n".join(list_)

    def competition_statistics(self):
        healthy_divers = [diver for diver in self.divers if not diver.has_health_issue]

        sorted_divers = sorted(
            healthy_divers,
            key=lambda x: (x.competition_points, len(x.catch), x.name),
            reverse=True
        )

        statistics_string = "**Nautical Catch Challenge Statistics**\n"
        for diver in sorted_divers:
            statistics_string += f"{diver}\n"

        return statistics_string




