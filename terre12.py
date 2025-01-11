################
# # 12 to 24 # #
################

import sys
import re

arguments = sys.argv[1:]
pattern = r"^(1[0-2]|0?[1-9]):([0-5][0-9])(AM|PM)$"
time = arguments[0]

if len(arguments) != 1:
    sys.exit("Tu ne me la mettras pas à l'envers.")

if not re.search(pattern, time):
    sys.exit("Erreur: format invalide.")

hours = int(time[:2])
minutes = time[3:5]
character_am = "AM"

if hours == 12 and character_am in time:
    hours = 0
elif hours != 12 and character_am not in time:
    hours += 12

print(f"{hours:02}:{minutes}")

