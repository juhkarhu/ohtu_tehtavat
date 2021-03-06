from statistics import Statistics
from player_reader import PlayerReader


def main():
    player_reader = PlayerReader()
    stats = Statistics(player_reader)
    philadelphia_flyers_players = stats.team("PHI")

    top_scorers = stats.top_scorers(10)

    arr = stats.top_scorers(1)
    print('top scorer', dir(arr))
    print('test', top_scorers)

    print("Philadelphia Flyers:")
    for player in philadelphia_flyers_players:
        print(player)

    print("Top scorers:")
    for player in top_scorers:
        print(player)


if __name__ == "__main__":
    main()
