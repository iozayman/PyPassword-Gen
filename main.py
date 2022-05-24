#Password Generator Project
import random
from random import randint
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#passw = ""
#for i in range(nr_letters):
#  passw += letters[random.randint(0,51)]
#for i in range(nr_symbols):
#  passw += symbols[random.randint(0,8)]
#for i in range(nr_numbers):
#  passw += numbers[random.randint(0,9)]
#print(passw)
  
  


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

##There are better ways like one line of code. That was a challenge.

ALOTOFEFORT = [letters, numbers, symbols]
passw = ""
l1= 0
l2= 0
howmany = nr_letters +nr_numbers + nr_symbols
n1= ""
for i in range (nr_letters):
  n1 += "0"
for i in range (nr_symbols):
  n1 += "1"
for i in range (nr_numbers):
  n1 += "2"
  

for i in range(howmany):
  l1 = int(random.choice(n1))
  if l1 == 0:
    l2 = randint(0,51)
  elif l1 == 1:
    l2 = randint(0,9)
  else:
    l2 = randint(0, 8)
  passw += ALOTOFEFORT[l1][l2]

print(passw)
    

  