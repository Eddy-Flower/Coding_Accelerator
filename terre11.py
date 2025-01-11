################
# # 24 to 12 # #
################

import sys
import re

arguments = sys.argv[1:]
pattern = r"^(2[0-3]|[01]?[0-9]):([0-5]?[0-9])$"
time = arguments[0]

if len(arguments) != 1:
    sys.exit("Tu ne me la mettras pas à l'envers.")

if not re.search(pattern, time):
    sys.exit("Erreur: format invalide.")

hours = int(time[:2])
minutes = time[3:5]
am_pm = hours - 12

if hours > 12:
    print(f"{am_pm}:{minutes}PM")
elif hours == 12:
    print(f"{hours}:{minutes}PM")
elif hours == 00:
    print(f"{hours + 12}:{minutes}AM")
else:
    print(f"{hours}:{minutes}AM")



