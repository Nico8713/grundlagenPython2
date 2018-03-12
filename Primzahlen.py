#primzahlen
#funktion: check if given number is prime
def isPrime(n):
    #logik einbauen
    if(n <= 1):
        return False

    for p in range(2,n):
         if(n % p == 0):
             return False

    return True




print("primzahlen-Checker")
z = input("Bitte die zahl eingeben: ")
z = int(z)
if (isPrime(z)):
    print(z, "Ist eine primzahl")
else:
    print(z, "ist KEINE Primzahl")
