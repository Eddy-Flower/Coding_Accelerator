######################
# # Nombre premier # #
######################

import sys

arguments = sys.argv[1:]

if len(arguments) != 1:
    sys.exit("Tu ne me la mettras pas à l'envers.")

for i in arguments:
    if not i.isdigit():
        sys.exit("Erreur : Tous les arguments doivent être des nombres "
                 "entiers strictement positif.")

if int(arguments[0]) <= 1:
    sys.exit("Attention : 0 et 1 ne sont pas des nombres premier. ")

number = int(arguments[0])

for i in range(2, number):
    if number % i == 0:  
        print(f"Non, {number} n'est pas un nombre premier.")
        break
    else:
        print(f"Oui, {number} est un nombre premier.")
        break
    

