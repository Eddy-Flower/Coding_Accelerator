### L’alphabet à partir de

import sys

for i in range(97, 123):
    if chr(i) >= sys.argv[1]:
        print(chr(i), end="")
print()

