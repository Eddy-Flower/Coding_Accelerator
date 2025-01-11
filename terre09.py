### Racine carré d'un nombre

import sys

arguments = sys.argv[1:]

if len(arguments) != 1:
    sys.exit("Tu ne me la mettras pas à l'envers.")

if not arguments[0].lstrip("-").isdigit():
    sys.exit("Erreur : Tous les arguments doivent être des nombres entiers.")

number = int(arguments[0])
square_root = 0

if number <= 0:
    sys.exit("Erreur : Le nombre entier doit être strictement positif")

for _ in range(number):
    if square_root * square_root == number:
        break
    square_root += 1

print("Ce nombre n'a pas de racine carré entière." if square_root >= number else square_root)


