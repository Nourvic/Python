# Methoden

#Funktion mit Rückgabewert
def potenz(n: int, k: int) -> int:
    return n ** k # ** ist der Exponentenoperator z.B.  n=3 , k=2 => 3^2 = 9
 
# Funktion ohne Rückgabewert:
def begrüße(name: str, formell: bool = False):
    if formell:
        print(f"Hallo {name}, wie geht es Ihnen?")
    else:
        print(f"Hallo {name}, wie geht's?")


# mann kan auch False weglassen, weil es schon als Standardwert in der Funktion gesetzt wurde
begrüße("Nour",True)
begrüße("Nour",False)
