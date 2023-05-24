import random

print('Welcome in the password generator')

chars = ('abcdefghilmnoprstqvzABCDEFGHILMNOPQRSVZ1234567890!"£$%&/()=?^')

number = input('Amount of password to generate')
number = int(number)

lenght = input('How long the password?')
lenght = int(lenght)

print('here is the password')

for pwd in range(number):
    passwords = ''
for c in range(lenght):
    passwords += random.choice(chars)
print(passwords)

//i have copy-pasted this, lol
