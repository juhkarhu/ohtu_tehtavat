class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.even_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.advantage()
        else:
            return self.odd_score()

    def even_score(self):
        if self.player1_score == 0:
            score = "Love-All"
        elif self.player1_score == 1:
            score = "Fifteen-All"
        elif self.player1_score == 2:
            score = "Thirty-All"
        elif self.player1_score == 3:
            score = "Forty-All"
        else:
            score = "Deuce"
        return score

    def advantage(self):
        advantage_for = self.player1_score - self. player2_score

        if advantage_for == 1:
            score = "Advantage player1"
        elif advantage_for == -1:
            score = "Advantage player2"
        elif advantage_for >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score

    def odd_score(self):
        score = ''

        for i in range(1, 3):
                if i == 1:
                    temp_score = self.player1_score
                else:
                    score = score + "-"
                    temp_score = self.player2_score

                if temp_score == 0:
                    score = score + "Love"
                elif temp_score == 1:
                    score = score + "Fifteen"
                elif temp_score == 2:
                    score = score + "Thirty"
                elif temp_score == 3:
                    score = score + "Forty"
        return score


