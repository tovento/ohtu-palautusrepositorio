class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()

        players_by_nationality = filter(
            lambda p: p.nationality == nationality,
            players
        )

        sorted_players = sorted(
        players_by_nationality,
        key=lambda player_: player_.points,
        reverse=True
        )

        return sorted_players
