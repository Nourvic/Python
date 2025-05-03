# ohne zeilenumbruch 
#for letter in "codezilla":
# print(letter,end="")

#ohne zeilen-umbruch 2
character = ["pikachu","grandizer","Scorpion","subzero"]
for chart in character:
    print(chart)

for index in range(10):
    if index %2 ==0:
        print(index,"ist eine gerade Zahl")
    else:
        print(index,"ist eine ungerade Zahl")

for buddy in range(len(character)):
    if character[buddy] == "Scorpion":
        print(buddy,"is the master")
    else:
        print(buddy,"Finish Him")

for buddy2 in character:
    if buddy2 =="subzero":
        break
    else:
        print(buddy2,"& Liu King are MK")