"""
Looks for needle in haystack and prints
start and stop indexes.
"""

haystack = """Bacon ipsum dolor amet tail ribeye biltong
    leberkas pork loin short loin tenderloin tri-tip
    kielbasa sausage pancetta. Brisket short loin
    shoulder alcatra picanha swine cupim. Capicola
    ground round tri-tip, pancetta pastrami short
    loin short ribs spare ribs buffalo chuck. Pork ball
    tip beef ribs, ham hock alcatra tenderloin
    frankfurter spare ribs jowl tail burgdoggen t-bone
    prosciutto. Kielbasa ball tip alcatra spare ribs
    chuck fatback shankle hambutt hock pig pork chop
    strip steak landjaeger. Hamburger porchetta
    frankfurter buffalo swine tongue.""".lower()

needle = input("Needle: ")

for index, letter in enumerate(haystack):
    if letter == needle[0]:
        same_word = True
        for needle_index, needle_letter in enumerate(needle):
            if haystack[index + needle_index] != needle_letter:
                same_word = False
                break
        if same_word:
            print("start: " + str(index) + ", slut: " + str(index + len(needle)))
