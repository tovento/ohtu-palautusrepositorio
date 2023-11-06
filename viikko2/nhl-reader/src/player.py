class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.points = self.goals + self.assists
    
    def __str__(self):
        return (
            f"{self.name:20} "
            f"{self.team} "
            f"{self.goals:2} + "
            f"{self.assists:2} = "
            f"{self.points}"
        )
