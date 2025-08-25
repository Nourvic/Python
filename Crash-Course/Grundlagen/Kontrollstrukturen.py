# IF -Statement

alter =18
if alter >= 18:
    print("er/sie ist Volljaehrig")
else:
    print("er/sie Minderjaehrig")

for i in range(5):
    print(i)
    
x:int=0
while alter <35:
    alter+=1
    x+=1
print("Wert  von X ist : ",x)


# IF - Statements

note = 3
if note == 1:
    print("Sehr gut")
elif note == 2:
    print("Gut")
elif note == 3:
    print("Befriedigend")
else:
    print("Verbesserungsbedarf")


# For-Schleife`

for x in ["a","b","c"]:
    print(x)
for y in range(5):
    print(y)


# While-Schleifes

alter =18
while alter <=35:
    alter+=1
    if alter == 21:
        break
    print(alter)

# examples

friends = [1,"Training",True,False,[1,"Nour"]]
print(friends)
print(friends[0])
print(friends[4])

friends2 = ["Studium","Ausbildung","Duales-Studium","Werkstudium"]
print(friends2[-1])
print(friends2[-4])
print(friends2[1:3]) # von index 1 bis 3, aber 3 wird nicht selektieret 
print(friends2[1:])  # von index 1 bis letzte Element

friends+=friends2
print(friends)

friends3 = friends2
friends3.append(False)
friends3.append([True,7])
friends3.insert(0,"Yuhooo")
print(friends3)
what_was_popped = friends3.pop()
print(what_was_popped)

friends4 = ["Programming","JAVA","TypeScript","Python"]
print(friends4.index("Python")) #liefert Platznummer von der Liste zurueck
# print(friends4.index("JavaScript")) # ist nicht in der Liste enthalten
friends4.append("JAVA")
anz =friends4.count("JAVA")
print(anz)
friends4.pop()
friends4.sort()
print(friends4)
