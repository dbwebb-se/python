"""
Skapa ett program som slumpar fram en rad från en fil.
Filen innehåller rader där {} ska bytas ut mot input från användaren.
Du får inte använda dig utav listor eller .format().
Den nya strängen, som skapas från rad i fil och
input från användaren, ska spara till en fil
som ska byggas på varje gång programmet körs.
"""
import random

def get_random_line():
    """
    Pick random string from file
    """
    with open("random_lines.txt", "r") as fd:
        all_text = fd.read()

    number_of_lines = all_text.count("\n")
    random_line = random.randint(1, number_of_lines)

    with open("random_lines.txt", "r") as fd:
        count = 1
        while count <= random_line:
            line = fd.readline().strip()
            count += 1

    return line

def output_line(formatted_line):
    """
    Write formatted string to file
    """
    with open("formatted_lines.txt", "a") as fd:
        fd.write(formatted_line + "\n")

def main():
    """
    Starting point of program
    """
    line = get_random_line()
    formatted_line = line.replace(
        "{}",
        input("Vad vill du ska in i strängen? ")
    )
    output_line(formatted_line)


if __name__ == "__main__":
    main()
