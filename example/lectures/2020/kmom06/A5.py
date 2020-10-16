"""
How assignment A5 in marvin can be solved with dictionary
"""
def transform_value(player, score):
    """
    Transform value to negative in if player is upper
    """
    if player.isupper():
        return -int(score)
    return int(score)


def calculate_score(results):
    """
    calculate score for all players
    """
    counter = 0
    tot_players = {}

    while counter < len(results):
        player = results[counter]
        score = results[counter+1]
        score = transform_value(player, score)

        player = player.lower()
        tot_players[player] = tot_players.get(player, 0) + score

        counter += 2
    print(tot_players)



if __name__ == "__main__":
    calculate_score("a2b4A5s3B1")
    calculate_score("g3l1H5l2G3l1")
