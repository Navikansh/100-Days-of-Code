import random

letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 
           'i', 'o', 'p', 'a', 's', 'd', 'f', 
           'g', 'h', 'j', 'k', 'l', 'z', 'x', 
           'c', 'v', 'b', 'n', 'm', 'Q', 'W', 
           'E', 'R', 'T', 'Y', 'U', 'I', 'O',
           'P', 'A', 'S', 'D', 'F', 'G', 'H', 
           'J', 'K', 'L', 'Z', 'X', 'C', 'V', 
           'B', 'N', 'M']

numbers = ['1', '2', '3', '4', '5', '6', '7', 
           '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', 
           '*', '(', ')']

nletters = int(input('How many letters? ').strip())
nnumbers = int(input('How many numbers? ').strip())
nsymbols = int(input('How many symbols? ').strip())
password = []

for i in range(1, nletters+1):
    passchar = random.choice(letters)
    password.append(passchar)
print(password)

for i in range(1, nnumbers+1):
    passnum = random.choice(numbers)
    password.append(passnum)
print(password)

for i in range(1, nsymbols+1):
    passsym = random.choice(symbols)
    password.append(passsym)
print(password)

random.shuffle(password)
pswrd = ''
for i in password:
    pswrd += i
print(pswrd)

