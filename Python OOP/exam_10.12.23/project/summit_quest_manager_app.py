from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    VALID_CLIMBER_TYPES = {"ArcticClimber": ArcticClimber, "SummitClimber": SummitClimber}
    VALID_PEAK_TYPES = {"ArcticPeak": ArcticPeak, "SummitPeak": SummitPeak}

    def __init__(self):
        self.climbers: List[object] = []
        self.peaks: List[object] = []

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.VALID_CLIMBER_TYPES:
            return f"{climber_type} doesn't exist in our register."

        climber_registered = next((c for c in self.climbers if climber_name == c.name), None)
        if climber_registered:
            return f"{climber_name} has been already registered."

        climber = self.VALID_CLIMBER_TYPES[climber_type](climber_name)
        self.climbers.append(climber)
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.VALID_PEAK_TYPES:
            return f"{peak_type} is an unknown type of peak."

        peak = self.VALID_PEAK_TYPES[peak_type](peak_name, peak_elevation)
        self.peaks.append(peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."


    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        peak = next((p for p in self.peaks if peak_name == p.name), None)
        gear_needed = peak.get_recommended_gear()
        climber = next((c for c in self.climbers if climber_name == c.name), None)

        missing_gear = []
        for g in gear_needed:
            if g not in gear:
                missing_gear.append(g)

        if missing_gear:
            climber.is_prepared = False
            return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted(missing_gear))}."
        return f"{climber_name} is prepared to climb {peak_name}."


    def perform_climbing(self, climber_name: str, peak_name: str):
        climber = next((c for c in self.climbers if climber_name == c.name), None)
        if not climber:
            return f"Climber {climber_name} is not registered yet."

        peak = next((p for p in self.peaks if peak_name == p.name), None)
        if not peak:
            return f"Peak {peak_name} is not part of the wish list."

        if climber.is_prepared and climber.can_climb():
            climber.climb(peak)
            climber.conquered_peaks.append(peak_name)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."

        else:
            if not climber.is_prepared:
                return f"{climber_name} will need to be better prepared next time."
            elif not climber.can_climb():
                return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        climber_with_conquered_peaks = [c for c in self.climbers if c.conquered_peaks]
        peaks_counter = sum(len(c.conquered_peaks) for c in climber_with_conquered_peaks)

        sorted_climbers = sorted(climber_with_conquered_peaks, key=lambda x: (-len(x.conquered_peaks), x.name))

        result = [f"Total climbed peaks: {peaks_counter}", "**Climber's statistics:**"]

        for climber in sorted_climbers:
            result.append(str(climber))

        return '\n'.join(result)





