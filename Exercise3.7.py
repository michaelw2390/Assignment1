# (Random character) Write a program that displays a random uppercase letter
# using the time.time() function

import time

random = int(time.time())

print((chr(ord('A') + random % 26)))

