#!/bin/python3

import math
import os
import random
import re
import sys

def counterduplicate1(strings):
    chars = "g"
    for z in chars:
        count=strings.count(z)
        if count == 2: return "ok"
        else: return "-1"

def counterduplicate2(strings):
    chars = "o"
    for z in chars:
        count=strings.count(z)
        if count == 2: return "ok"
        else: return "-1"

    
def estimatedvalue(strings):
    strings=strings.lower()
    if (strings.find('g') != -1 or strings.find('o') != -1 or strings.find('e') != -1 or strings.find('3') != -1  or strings.find('<>') != -1 or strings.find('[]') != -1  or strings.find('i') != -1 or strings.find('0') != -1) and (strings.find(' ') == -1) and (counterduplicate1(strings) == "ok" or counterduplicate2(strings) == "ok") and (len(strings)<=8 and len(strings) >= 6) and ( strings[-1] == '3' or strings[-1] == 'e') and (strings[-3] == 'g') and (strings[-4] == ">" or strings[-4] == ")" or strings[-4] == "]" or strings[-4] == "o" or strings[-4] == '0' ): return "True"
    else: return "False"


if __name__ == '__main__':
    strings = input()
    print(estimatedvalue(strings))
    # Create your code here
