def get_letter_values(score_string):
    scores = {}
    for letter in score_string:
        scores[letter] = scores.get(letter, 0) + 1

    return scores

def fix_multiplier(multiplier_string):
    multiplier_list = multiplier_string.split(",")
    multiplier_integer_list = []

    for multiplier in multiplier_list:
        multiplier_integer_list.append(int(multiplier))

    return multiplier_integer_list


def calculate_score(word, letter_values):
    total_score = 0

    for letter in word:
        total_score += letter_values.get(letter, 0)

    print(word + " equals " + str(total_score) + " points")

def main():
    score_string = "xygkjjfzqfdmqvbyzemcvywkizxxvxmpgaxqzwthqbjjqjzjvhwpxzkudqrcxkqzphhzcszykbzflfjqqqonxjw"
    letter_values = get_letter_values(score_string)

    word = input("Input word: ")
    multiplier = input("Input multiplier: ")

    calculate_score(
        word,
        letter_values,
        fix_multiplier(multiplier)
    )

if __name__ == "__main__":
    main()
