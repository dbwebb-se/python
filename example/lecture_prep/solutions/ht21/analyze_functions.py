"""
Analysera myths.txt
"""
def read_file():
    """
    returns file as paragrafs in a list
    """
    with open("myths.txt", "r") as fh:
        paragraf = ""
        first_newline = 0
        for char in fh.read():
            if char != "\n":
                paragraf += char
            else:
                if first_newline:
                    first_newline = 0
                    yield paragraf
                    paragraf = ""
                else:
                    first_newline = 1

def count_sentences():
    """
    antalet meningar som finns i varje paragraph beräknas
    Skriv ut antalet meningar som finns i de tre paragrafer som har flest meningar.
    Skriv enbart ut siffran sorterad från högst till lägst
    """
    # paragrafs = read_file()
    # nr_of_sentences = []
    # for paragraf in paragrafs:
    #     nr_of_sentences.append(paragraf.count("."))
    # nr_of_sentences = [paragraf.count(".") for paragraf in paragrafs]
    # nr_of_sentences.sort(reverse=True)
    print(
        sorted(
            [paragraf.count(".") for paragraf in read_file()],
            reverse=True
        )[:3]
    )



def count_gods():
    """
    räkna hur många gånger gudarnas namn nämns i varje paragraf
    För topp tre paragrafer skriv ut antalet gånger gudarna nämns
     sorterad från högst tilllägst
    """
    gods = "Odin,Thor,Hödur,Baldur,Tyr,Heimdall,Vidar,Vali,Loki,Frigga,Freya,Nanna,Iduna,Sif,Modi,Magni"
    paragrafs = read_file()
    # nr_of_gods = []
    # for paragraf in paragrafs:
    #     god_sum = 0
    #     for god in gods.split(","):
    #         god_sum += paragraf.count(god)
    #     nr_of_gods.append(god_sum)
    
    nr_of_gods = sorted(
        [sum([paragraf.count(god) for god in gods.split(",")]) for paragraf in paragrafs],
        reverse=True
    )[:3]
    print(nr_of_gods)
