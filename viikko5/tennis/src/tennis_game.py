SCORES = {
    0: "Love",
    1: "Fifteen",
    2: "Thirty",
    3: "Forty"}


class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.even_game():
            return self.even_scores()

        elif self.score_higher_than_forty():
            difference = self.difference_in_scores()
            if difference == 1:
                if self.player1_leading():
                    return "Advantage player1"
                else:
                     return "Advantage player2"
            elif difference >= 2:
                if self.player1_leading():
                    return "Win for player1"
                else:
                    return "Win for player2"
        return f"{SCORES[self.player1_score]}-{SCORES[self.player2_score]}"

    def even_game(self):
        return self.player1_score == self.player2_score

    def even_scores(self):
        if self.deuce(self.player1_score):
            return "Deuce"
        return f"{SCORES[self.player1_score]}-All"

    def deuce(self, even_score):
        return even_score > 2

    def score_higher_than_forty(self):
        return self.player1_score > 3 or self.player2_score > 3

    def player1_leading(self):
        return self.player1_score > self.player2_score

    def difference_in_scores(self):
        return abs(self.player1_score - self.player2_score)
