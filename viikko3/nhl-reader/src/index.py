import requests
from PlayerReader import PlayerReader
from PlayerStats import PlayerStats
from player import Player
from datetime import datetime


    
def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)




if __name__ == "__main__":
    main()
