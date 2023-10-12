name = "Tony Stark"
age = 51
is_genius = True
print("You are", name, "of age", age, ".\nIt is", is_genius, "that you are a genius.")
hero_name = input("What's your name as a superhero? ")
print("So you are", hero_name, ".")

team = {}

for i in range(100):
    mem = input("Enter the name of " + str(100 - i) + " more members of AVENGERS or type exit. ")
    if mem.lower() == "exit":
        print("Alright.")
        break
    else:
        power = input("Enter their best ability: ")
        team[mem] = power

print("Total number of members are:", len(team), ".")
if len(team) == 0:
    pass
else:
    print("Here they are:\n")
    print(team)