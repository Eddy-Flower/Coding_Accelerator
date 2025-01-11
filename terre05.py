### Divisions

import sys

arguments = sys.argv[1:]

if len(arguments) != 2:
    sys.exit("Tu ne me la mettras pas à l'envers.")

for i in arguments:
    if not i.isdigit():
        sys.exit("Tape un nombre valide.")

dividend = int(arguments[0])
divisor = int(arguments[1])
quotient = 0
remainder = dividend

for _ in range(dividend):
    if remainder < divisor:
        break
    remainder -= divisor
    quotient += 1

if divisor > dividend:
    print("Erreur : le diviseur est plus grand que le dividende.")
else:
    print(f"quotient: {quotient}")
    print(f"remainder: {remainder}")

