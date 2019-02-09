#!/usr/local/bin/python
from random import randrange

def roll(CdS):
    (count, sides) = map(int, CdS.split("d"))
    sum = 0
    rolls = []
    if 1 <= count <= 100 and 2 <= sides <= 100:
        for i in range(0,count):
            tmp = randrange(1, sides+1)
            sum = sum + tmp
            rolls.append(str(tmp))
        rollString = " ".join(rolls)
        print(f'{sum}: {rollString}')
    else:
        print("")
