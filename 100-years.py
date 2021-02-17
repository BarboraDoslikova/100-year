# -*- coding: utf-8 -*-
"""
Created on 17.02.2021
This script asks the user to enter their name and age, 
then prints out a message addressed to them
that tells them the year that they will turn 100 years old.
@author: Barbora Doslikova
"""

import datetime

# gather user info
username = input('what is your name? ')
userage = int(input('what is your age? '))

# calculate output
currentyearauto = datetime.datetime.now().year
hundredyear = str(currentyearauto + (100-userage))

# prepare output
outputsentence = "Hello " + username + "! You will turn 100 in the year " + hundredyear + "."

# print output
print(outputsentence)
