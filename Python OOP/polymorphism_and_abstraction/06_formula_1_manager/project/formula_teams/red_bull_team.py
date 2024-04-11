from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    EXPENSES_PER_RACE = -250000
    ORACLE_REVENUE = {1: 1500000, 2: 800000}
    HONDA_REVENUE = {1: 20000, 2: 20000, 3: 20000, 4: 20000, 5: 20000, 6: 20000, 7: 20000, 8: 20000, 9: 10000, 10: 10000}

    def calculate_revenue_after_race(self, race_pos: int):
        current_race_revenue = self.EXPENSES_PER_RACE
        if race_pos in self.ORACLE_REVENUE:
            current_race_revenue += self.HONDA_REVENUE[race_pos] + self.ORACLE_REVENUE[race_pos]
        elif race_pos in self.HONDA_REVENUE:
            current_race_revenue += self.HONDA_REVENUE[race_pos]
        self.budget += current_race_revenue
        return f"The revenue after the race is {current_race_revenue}$. Current budget {self.budget}$"


