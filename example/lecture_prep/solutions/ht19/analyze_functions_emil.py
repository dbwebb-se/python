"""
Analyzes myths.txt
"""

def read_file_and_split_on_paragraphs():
    """
    Reads file and splits on paragraphs
    """
    with open("myths.txt") as fh:
        myth_text = fh.read()
        return myth_text.split("\n\n")

def top_3(high_score):
    """
    Prints top 3
    """
    for score in sorted(high_score, reverse=True)[0:3]:
        print(score)

def sentences():
    """
    Counts sentences in paragraphs
    """
    paragraphs = read_file_and_split_on_paragraphs()
    high_score = []
    for paragraph in paragraphs:
        number_of_sentences = paragraph.count(".")
        high_score.append(number_of_sentences)

    top_3(high_score)

def gods():
    """
    Counts the gods in each paragraph
    """
    all_gods = [
        "Odin", "Thor", "Hödur", "Baldur", "Tyr",
        "Heimdall", "Vidar", "Vali", "Loki", "Frigga",
        "Freya", "Nanna", "Iduna", "Sif", "Modi", "Magni"
        ]

    paragraphs = read_file_and_split_on_paragraphs()
    high_score = []
    for paragraph in paragraphs:
        paragraph = paragraph.replace(".", "").replace(",", "").replace(";", "")
        words = paragraph.split(" ")

        score = 0
        for word in words:
            if word in all_gods:
                score += 1

        high_score.append(score)

    top_3(high_score)
