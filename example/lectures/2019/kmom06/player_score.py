"""
Dictionary example.
Solves extra assigment A5 of marvin2.
https://dbwebb.se/uppgift/din-egen-chattbot-marvin-steg-1-v2#extra
"""
def transform_number(char, number):
    """
    Make number an in and negative i player is upper.
    """
    if char.isupper():
        return -int(number)
    return int(number)

def calc_player_score():
    """
    Calculate players score based on a string
    """
    string = input("Enter score string: ")
    # "a2b4A5s3B1"
    count = 0
    players = {}
    while count < len(string):
        player = string[count]
        if player.isalpha():
            score = transform_number(player, string[count+1])
            players[player.lower()] = players.get(player.lower(), 0) + score
        count += 2
    return players

def print_soreted_dict(players):
    """
    Print players score in score order
    """
    for player in sorted(players, key=players.get):
        print(player, "has", players[player], "points")

if __name__ == "__main__":
    players_score = calc_player_score()
    print_soreted_dict(players_score)
