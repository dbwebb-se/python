"""
Programmet skriver tar namn och ålder som input från användaren.
Värdena användaren skriver in används för att skapa en hälsning med namn, ålder och födelse år.
"""

year = 2017 # Hårdkodat värde för vilket år det är

name = input("Skriv ett namn, klicka sen enter: ") # Ber användaren mata in ett namn
age = input("Skriv en ålder, klicka sen enter: ") # Ber användaren mata in en ålder

year_born = str(year - int(age)) # Födelse år räknas ut. Gör om age från string till integer med int()

greeting = "Hej " + name + ", du är " + age + " år gammal och föddes år " + year_born # Sätter ihop "Hej", name, ", du är ", age och " år gammal." till ett värde.
print(greeting) # Skriver ut ett string värde