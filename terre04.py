### Pair ou impair

import sys

arguments = sys.argv[1:]

if len(arguments) != 1:
    sys.exit("Tu ne me la mettras pas à l'envers.")

if not arguments[0].lstrip("-").isdigit():
    sys.exit("Tape un nombre valide.")

if int(arguments[0]) % 2 == 0:
    print(int(arguments[0]), "est un nombre pair.")
else:
    print(int(arguments[0]), "est un nombre impair.")

