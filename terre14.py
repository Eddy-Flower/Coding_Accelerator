###################
# # Trié ou pas # #
###################
 
import sys

arguments = sys.argv[1:]

if len(arguments) < 2:
    sys.exit("Tu ne me la mettras pas à l'envers.")

for i in arguments:
    if not i.isdigit():
        sys.exit("Erreur : Tous les arguments doivent être des "
                 "nombres entiers strictement positif.")

for i in range(len(arguments)-1):
    if not int(arguments[i]) <= int(arguments[i+1]):
        sys.exit("Pas trié !")
print("Trié !")

