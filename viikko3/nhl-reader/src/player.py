class Player(object):
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games




    def __str__(self):
        #return f"{str(self.name):2} team {self.team}, goals {self.goals} assists {self.assists}"
        return f"{self.name:20} {self.team} {self.goals} + {self.assists} = {self.goals + self.assists}"
