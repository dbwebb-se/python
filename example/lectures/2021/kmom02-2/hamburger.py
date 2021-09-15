"""
Skriv ett program som ska hitta vilken index position en substräng
 startar och slutar på i en större sträng. Ex substrängen "j e" börjar på
  index 2 och slutar på 4 i "Hej Emil".

I din lösning får du inte använda några inbyggda funktioner förutom range(), enumerate() och lower().

Exempel input: "Bacon ipsum dolor amet tail ribeye biltong leberkas pork
 loin short loin tenderloin tri-tip kielbasa sausage pancetta. 
 Brisket short loin shoulder alcatra picanha swine cupim. 
 Capicola ground round tri-tip, pancetta pastrami short loin short ribs
 spare ribs buffalo chuck. Pork ball tip beef ribs, ham hock alcatra
 tenderloin frankfurter spare ribs jowl tail burgdoggen t-bone
 prosciutto. Kielbasa ball tip alcatra spare ribs chuck fatback 
 shankle hambutt hock pig pork chop strip steak landjaeger.
 Hamburger porchetta frankfurter buffalo swine tongue."
"hamburger"
Output: start: 500, slut: 509
"""
needle = "prosciutto"
haystack = """Bacon ipsum dolor amet tail ribeye biltong leberkas pork
 loin short loin tenderloin tri-tip kielbasa sausage pancetta. 
 Brisket short loin shoulder alcatra picanha swine cupim. 
 Capicola ground round tri-tip, pancetta pastrami short loin short ribs
 spare ribs buffalo chuck. Pork ball tip beef ribs, ham hock alcatra
 tenderloin frankfurter spare ribs jowl tail burgdoggen t-bone
 prosciutto. Kielbasa ball tip alcatra spare ribs chuck fatback 
 shankle hambutt hock pig pork chop strip steak landjaeger.
 Hamburger porchetta frankfurter buffalo swine tongue.""".lower()

length_of_needle = len(needle)
for index, letter in enumerate(haystack[:-length_of_needle]):
    if haystack[index:index + length_of_needle] == needle:
        print(haystack[index:index + length_of_needle])
        print("start: {}, slut: {}".format(index + 1, index + 1 + length_of_needle))
