from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    EXPENSES_PER_RACE = -200000
    PETRONAS_REVENUE = {1: 1000000, 2: 500000, 3: 500000}
    TEAMVIWER_REVENUE = {1: 100000, 2: 100000, 3: 100000, 4: 100000, 5: 100000, 6: 50000, 7: 50000}

    def calculate_revenue_after_race(self, race_pos: int):
        current_race_revenue = self.EXPENSES_PER_RACE
        if race_pos in self.PETRONAS_REVENUE:
            current_race_revenue += self.PETRONAS_REVENUE[race_pos] + self.TEAMVIWER_REVENUE[race_pos]
        elif race_pos in self.TEAMVIWER_REVENUE:
            current_race_revenue += self.TEAMVIWER_REVENUE[race_pos]
        self.budget += current_race_revenue
        return f"The revenue after the race is {current_race_revenue}$. Current budget {self.budget}$"