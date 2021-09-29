"""
Skriv en funktion som tar emot en lista som innehåller heltal och en (1) nivå av nestlade listor, även dessa med heltal.

Iterera igenom listan och summera alla siffror i förälder listan. 
Varje gång du stöter på en barn lista summera siffrorna i denna och 
skriv ut barnlistans summa. Addera barnlistornas summa till förälderlistans totala summa.

Listor att testa med:

[1, 2, 3, 4]
[1, 2, [6, 7, 8], 5, 7, 9]
[[1, 2], [6, 7, 8], [5, 7, 9], [7, 9, 13], 2]
"""

def sum_sublist(items):
    """
    sums list of integers
    """
    sub_total = 0
    
    for number in items:
        sub_total += number
        
    print("subtotal av " + str(items) + " är " + str(sub_total))
    
    return sub_total

def list_summer(items):
    """
    sums list
    """
    total = 0
    
    for number_or_list in items:
        if isinstance(number_or_list, list):
            total += sum_sublist(number_or_list)
        else:
            total += number_or_list
        
    print("Le grande total: " + str(total))
    
    
if __name__ == "__main__":
    numbers_and_list_list = [[1, 2], [6, 7, 8], [5, 7, 9], [7, 9, 13], 2]
    
    list_summer(numbers_and_list_list)
