"""
Skapa ett program där en dictionary används för att spara information om spelare. 
Spelare kan läggas in med handicap och sedan kan resultatet på varje hål 
läggas in i en lista av tuples efterhand som spelet fortgår.
"""

def create_players():
    """
    create players dict
    """
    players = {}
    inp = input("Enter 'name, handicap':")
    while inp != "done":
        name, handicap = inp.split(", ")
        players[name] = (int(handicap), []) # (number, pair, nr_shots)
        inp = input("Enter 'name, handicap':")
    return players

def play_game(players):
    """
    Add game data to players
    """
    inp = input("Enter 'name, course, nrumber for pair, number of shots':")
    while inp != "done":
        name, course, pair, nr_shots = inp.split(", ")
        players[name][1].append(
            (int(course), int(pair), int(nr_shots))
        ) 
        inp = input("Enter 'name, course, nrumber for pair, number of shots':")

def print_game(players):
    """
    Print game data pretty
    """
    HANDICAP_INDEX = 0
    GAME_HISTORY_INDEX = 1
    output = ""
    for name, games in players.items():
        output += f"{name} spelade följande med handikap {games[HANDICAP_INDEX]}:\n"
        for course, pair, nr_shots in games[GAME_HISTORY_INDEX]:
            output += f"\thål: {course} har par {pair} och spelare slog {nr_shots} slag\n"
    print(output)


if __name__ == "__main__":
    players_dict = create_players()
    play_game(players_dict)
    # players_dict = {
    #     "andreas": (10, [(1, 3, 2), (2, 4, 5)]),
    #     "emil": (10, [(1, 3, 3), (2, 4, 3)])
    # }
    print_game(players_dict)
