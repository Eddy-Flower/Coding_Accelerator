### Inverser une chaîne

import sys
arguments = sys.argv[1:]

if len(arguments) != 1:
    sys.exit("Tu ne me la mettras pas à l'envers.")

if arguments[0].isdigit():
    sys.exit("Tape des lettres de l'alphabet")

string = arguments[0]
reversed_string = ""

for i in range(len(string)-1,-1,-1):
    reversed_string += string[i]
print(reversed_string, end="")


