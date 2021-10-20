"""
Analysera myths.txt
"""
def read_file():
    """
    returns file as paragrafs in a list
    """
    with open("myths.txt", "r") as fh:
        return fh.read().split("\n\n")

def count_sentences():
    """
    antalet meningar som finns i varje paragraph beräknas
    Skriv ut antalet meningar som finns i de tre paragrafer som har flest meningar.
    Skriv enbart ut siffran sorterad från högst till lägst
    """
    paragrafs = read_file()
    nr_of_sentences = []
    for paragraf in paragrafs:
        nr_of_sentences.append(paragraf.count("."))
    nr_of_sentences.sort(reverse=True)
    print(nr_of_sentences[:3])

def count_gods():
    """
    räkna hur många gånger gudarnas namn nämns i varje paragraf
    För topp tre paragrafer skriv ut antalet gånger gudarna nämns
     sorterad från högst tilllägst
    """
    gods = "Odin,Thor,Hödur,Baldur,Tyr,Heimdall,Vidar,Vali,Loki,Frigga,Freya,Nanna,Iduna,Sif,Modi,Magni"
    paragrafs = read_file()
    nr_of_gods = []
    for paragraf in paragrafs:
        god_sum = 0
        for god in gods.split(","):
            god_sum += paragraf.count(god)
        nr_of_gods.append(god_sum)
    nr_of_gods.sort(reverse=True)
    print(nr_of_gods[:3])
