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
def calculate_points_per_letter(point_str):
    """
    Calculate each the points for each letter, build a dictionary with letter as key and its
    point as value and return the dictionary. This dictionary is used when calculating the 
    points for a word in function 'calculate_points_for_word'.
    """
    letter_dict = {}
    
    for letter in point_str:
        # instead of the if-statements below, if letter is not in letter_dic
        # the get function returns 0.
        letter_dict[letter] = letter_dict.get(letter, 0) + 1    
        """ if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1 """
    return letter_dict
    
def calculate_points_for_word(letter_dict, word):
    """
    Calculates the points for a word and return the point as an integer. 
    """
    total = 0
    
    for letter in word.lower():
        total += letter_dict[letter]
        
    return total

def calculate_points_for_word2(letter_dict, word, multipliers=None):
    """
    Calculates the points for a word and return the point as an integer. 
    """
    total = 0
    for index, letter in enumerate(word.lower()):
        if multipliers:
            total += letter_dict[letter] * multipliers[index]
        else:
            total += letter_dict[letter]
        
    return total


if __name__ == "__main__":
    letter_dict_ = calculate_points_per_letter(
        "xygkjjfzqfdmqvbyzemcvywkizxxvxmpgaxqzwthqbjjqjz\
jvhwpxzkudqrcxkqzphhzcszykbzflfjqqqonxjw"
    )
    
    word_ = "hello"
    print(word_, calculate_points_for_word2(letter_dict_, word_))

    word_ = "Maximize"
    print(word_, calculate_points_for_word2(letter_dict_, word_))

    print("With multiplier")
    print(word_, calculate_points_for_word2(letter_dict_, "hello", [3, 1, 1, 1, 1]))
    print(word_, calculate_points_for_word2(letter_dict_, "Maximize", [1, 1, 2, 1, 1, 1, 3, 1]))
