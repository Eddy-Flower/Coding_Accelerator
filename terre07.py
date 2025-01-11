### Taille d’une chaîne

import sys

arguments = sys.argv[1:]

if len(arguments) != 1:
    sys.exit("Tu ne me la mettras pas à l'envers.")

if arguments[0].isdigit():
    sys.exit("Tape des lettres de l'alphabet")

string = arguments[0]
counter = 0

for _ in string:
    counter += 1
print(counter, end="")


