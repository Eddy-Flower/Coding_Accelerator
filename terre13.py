###############################
# # Trouver la Suisse (lol) # #
###############################

import sys

arguments = sys.argv[1:]

if len(arguments) != 3:
    sys.exit("Tu ne me la mettras pas à l'envers.")

for i in arguments:
    if not i.isdigit():
        sys.exit("Erreur : Tous les arguments doivent être des "
                 "nombres entiers strictement positif.")

num1 = int(arguments[0])
num2 = int(arguments[1])
num3 = int(arguments[2])

if num1 == num2 or num1 == num3 or num2 == num3:
    sys.exit("Erreur : Il faut 3 nombres différent.")

if num2 < num1 < num3 or num3 < num1 < num2:
    print(num1)
elif num1 < num2 < num3 or num3 < num2 < num1:
    print(num2)
else:
    print(num3)

