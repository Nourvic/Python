# Liste mit Zahlen (einige Zahlen sind doppelt vorhanden)
numbers = [4, 3, 1, 2, 6, 7, 8, 9, 2, 1, 4, 2, 3, 4, 5, 1, 2, 4, 6, 7, 9, 5, 3, 1, 6, 8, 1, 2, 4, 0, 0, 0]

# Leere Liste für eindeutige Zahlen erstellen
zahlen = []
for zahl in numbers:
    if zahl not in zahlen:  # Nur neue Zahlen hinzufügen
        zahlen.append(zahl)

# Ausgabe der eindeutigen Zahlen ohne set()
print(zahlen)

# Schneller mit set(): erstellt eine Menge ohne Duplikate
zahlen_set = set(numbers)
print(zahlen_set)

# Der Typ von zahlen_set ist ein set-Objekt
print(type(zahlen_set))

# Alle Methoden und Attribute, die ein set-Objekt hat
print(dir(zahlen_set))

# Zusammenfassung:
# Mit set() entferne ich doppelte Werte einfach und habe viele Methoden zur Bearbeitung.

# Beispiel 2: Arbeiten mit Zeichenketten und set()
name = "Nour"  # Ein Name als String

# Umwandlung in ein Set: Jedes Zeichen wird ein einzelnes Set-Element (Reihenfolge geht verloren)
name_set = set(name)
print(name_set)

# Umwandlung des Sets in eine Liste, um Elemente bearbeiten zu können
namelist_set = list(name_set)

# Ein neues Element ('S') an die Liste anhängen
namelist_set.append('S')
print(namelist_set)
