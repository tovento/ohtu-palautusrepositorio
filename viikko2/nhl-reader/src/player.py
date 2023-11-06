class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
    
    def __str__(self):
        return (
            f"{self.name} "
            f"team {self.team} "
            f"goals {self.goals} "
            f"assists {self.assists}"
        )
