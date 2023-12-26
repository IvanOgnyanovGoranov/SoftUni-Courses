class Controller:
    VALID_TYPES = [
        "Food",
        "Drink"
    ]
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        players_added = []

        for player in players:
            if player not in players_added:
                players_added.append(player)
                self.players.append(player)

        return f"Successfully added: {', '.join(p.name for p in players_added)}"

    def add_supply(self, *supplies):
        [self.supplies.append(supply) for supply in supplies]

    def sustain(self, player_name: str, sustenance_type: str):
        if sustenance_type not in self.VALID_TYPES:
            return

        for player in self.players:
            if player.name == player_name:
                break
        else:
            return

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        for i in range(len(self.supplies)-1, -1, -1):
            supply = self.supplies[i]

            if supply.__class__.__name__ == sustenance_type:
                self.supplies.pop()
                break
        else:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        if player.stamina + supply.energy > 100:
            player.stamina = 100
        else:
            player.stamina += supply.energy

        return f"{player_name} sustained successfully with {supply.name}"

    def duel(self, first_player_name: str, second_player_name: str):
        currents_players = sorted([
            next(filter(lambda p: p.name == first_player_name, self.players)),
            next(filter(lambda p: p.name == second_player_name, self.players))
        ], key=lambda p: p.stamina)

        errors_list = []

        for player in players:
            if player.stamina <= 0:
                errors_list.append(f"Player {player.name} does not have enough stamina")

        if errors_list:
            return "\n".join(errors_list)

        return self.fight(currents_players)

    def fight(self, current_players) -> str:
        first_player_damage = current_players[0].stamina / 2

        if current_players[1].stamina <= first_player_damage:
            current_players[1].stamina = 0
            return f"Winner: {current_players[0].name}"
        else:
            current_players[1].stamina -= first_player_damage

        second_player_damage = current_players[1].stamina / 2

        if current_players[0].stamina <= second_player_damage:
            current_players[0].stamina = 0
            return f"Winner: {current_players[1].name}"
        else:
            current_players[0].stamina -= second_player_damage

        winner = sorted(current_players, key=lambda p: -p.stamina)[0]

        return f"Winner: {winner}"
