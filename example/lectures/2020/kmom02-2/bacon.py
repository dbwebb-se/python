text = "bacon ipsum dolor amet tail ribeye biltong leberkas pork loin short loin tenderloin tri-tip kielbasa sausage pancetta. Brisket short loin shoulder alcatra picanha swine cupim. Capicola ground round tri-tip, pancetta pastrami short loin short ribs spare ribs buffalo chuck. Pork ball tip beef ribs, ham hock alcatra tenderloin frankfurter spare ribs jowl tail burgdoggen t-bone prosciutto. Kielbasa ball tip alcatra spare ribs chuck fatback shankle hambutt hock pig pork chop strip steak landjaeger. Hamburger porchetta frankfurter buffalo swine tongue."
find = "hamburger"

for ind, letter in enumerate(text.lower()):
    if ind == 499:
        pass
    if letter == find[0]:
        found = True
        for ind2 in range(len(find)-1):
            if find[ind2+1] != text.lower()[ind+ind2+1]:
                found = False
                break
        if found:
            print(f"Found {find}, start: {ind}, stop: {ind+ind2+1}")
            
