#variable
'''
a = 10
b = 20
summe = a + b

print("summe von ", a," + ", b, "=", summe)

aktion = input("Welche Aktion willst du? (+/-/*/:)")
print("Aktion ", aktion, "wird ausgeführt...")

if(aktion == "*")
    print("Multiplikation ausgewählt")

zahl = input("welche zahl willst du?")
zahl = int(zahl)

zahl2 = int("23")

zahlA = "123"
zahlB = "456"
print(zahlA + zahlB)
'''



zahl1 = input("geben sie bitte eine zahl ein")
aktion = input("geben sie bitte eine aktion ein: (+/*/-//)")
zahl2 = input("bitte geben sie eine zweite zahl ein")

zahl1 = int(zahl1)
zahl2 = int(zahl2)


if (aktion == "+"):
    print("Sie haben die Addition gewählt")
    summe = zahl1 + zahl2

if (aktion == "-"):
    print("Sie haben die Subtraktion gewählt")
    summe = zahl1 - zahl2

if (aktion == "*"):
    print("Sie haben die Multiplikation gewählt")
    summe = zahl1 * zahl2

if (aktion == "/"):
    print("Sie haben die Division gewählt")
    summe = zahl1 / zahl2

print(summe)
