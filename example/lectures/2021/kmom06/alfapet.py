"""
Du ska skapa en poäng räknare för Alfapet. Varje bokstav är värd en viss poäng,
ex. ordet "Hello" är värt 8 poäng. "h" är värt 4 och 
resten av bokstäverna är värda 1 poäng.

För att få reda på varje bokstavs poäng behöver du parse följande sträng:
"xygkjjfzqfdmqvbyzemcvywkizxxvxmpgaxqzwthqbjjqjzjvhwpxzkudqrcxkqzphhzcszykbzflfjqqqonxjw"
varje bokstav är med så många gånger som den är värd. "h" är med 4 gånger. 
Skriv en funktion som tar emot en sträng och räknar ut dess poäng.

Extra: Funktionen ska även klara av multipliers, en lista med en multiplier
 för varje bokstav. "hello", [3, 1, 1, 1, 1] ger 16 poäng.

        Test:
        Input “hello” → 8, [3, 1, 1, 1, 1] → 16
        Input “world” → 9, [1, 2, 1, 1, 2] → 12
        Input “Maximize” → 28, [1, 1, 2, 1, 1, 1, 3, 1] → 56
        Input “Flapjack” → 26, [1, 1, 1, 1, 1, 1, 1, 1] → 26
                    
"""
def calculate_points(point_str):
    """
    Calculate each letters point worth
    """
    letter_dict = {}
    
    for letter in point_str:
        letter_dict[letter] = letter_dict.get(letter, 0) + 1    
    return letter_dict
    
def calculate_points_for_word(letter_dict, word):
    """
    calculates points for a word 
    """
    total = 0
    
    for letter in word.lower():
        total += letter_dict[letter]
        
    print(word, total)


if __name__ == "__main__":
    letter_dict_ = calculate_points(
        "xygkjjfzqfdmqvbyzemcvywkizxxvxmpgaxqzwthqbjjqjz\
jvhwpxzkudqrcxkqzphhzcszykbzflfjqqqonxjw"
    )
    
    word_ = "Maximize"
    calculate_points_for_word(letter_dict_, word_)
