def open_file():
   """
   read file content
   """
   try:
       # fd = open("data.txt", "r")
       with open("manifesto.txt", "r") as fd:
           return fd.read()
   except FileNotFoundError:
       print("You are missing the file")
   return None


def add_line():
   """
   add new line to file
   """
   new_line = input("Enter new line: ")
   with open("data.txt","a") as fd:
       fd.write("\n" + new_line)


def menu():
   """
   Main menu for program
   """
   while True:
       inp = input("""Enter option:
1. Read replace
2. insert new line
3. remove line
""")
       if inp == "1":
           print(open_file())
       elif inp == "2":
           add_line()
       elif inp == "3":
           pass
       else:
           exit()


if __name__ == "__main__":
   menu()
