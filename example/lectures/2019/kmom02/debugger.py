"""
Lets debug!
"""
import pdb
variable = """
Phil played two or three times more, managing to obtain in all
twenty-five cents additional. He reached the corner of Thirteenth Street
just as the large public school, known as the Thirteenth Street School,
was dismissed for its noon intermission."""

something = """,".:-'?"""
variable = variable.lower()
house = 0
for lobster in variable:
    if lobster in something:
        pdb.set_trace()
        house += 1
print(house)
