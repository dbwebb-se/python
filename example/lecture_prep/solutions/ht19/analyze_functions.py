"""
Analyzes myths.txt
"""

def read_file_and_split_on_paragraphs():
    """
    Reads file and splits on paragraphs
    """
    with open("myths.txt") as fh:
        for row in fh.read().split("\n\n"):
            yield row

def top_3(high_score):
    """
    Prints top 3
    """
    print("\n".join([str(score) for score in sorted(high_score, reverse=True)[0:3]]))

def sentences():
    """
    Counts sentences in paragraphs
    """
    high_score = [row.count(".") for row in read_file_and_split_on_paragraphs()]
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

    top_3([sum([paragraph.count(god) for god in all_gods])\
        for paragraph in read_file_and_split_on_paragraphs()])
