import os
from time import sleep

def screen_clear():
    os.system('clear')
print (" Platform", os.name)
print("big output\n" * 5)
sleep(5)
screen_clear()
