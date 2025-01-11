### Puissance d'un nombre

import sys

arguments = sys.argv[1:]

if len(arguments) != 2:
    sys.exit("Tu ne me la mettras pas à l'envers.")

for i in arguments:
    if not i.lstrip("-").isdigit():
        sys.exit("Erreur : Tous les arguments doivent être des nombres entiers.")

if int(arguments[1]) <= 0:
    sys.exit("Erreur : L’exposant doit être strictement positif")
    
base = int(arguments[0])
exponent = int(arguments[1])
power = 1

for _ in range(exponent):
    power *= base

print(power)



