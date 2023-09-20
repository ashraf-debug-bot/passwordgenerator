import random

password = ''
ch = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbol=['!','"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '{', '|', '}','~']
nu=['1', '2', '3','4', '5',' 6', '7', '8', '9', '10']
letter = int(input("Enter the number of  character ="))
sym=int(input("enter the number of symbols ="))
number=int(input("enter the number of character ="))
for i in range(1, letter+1):
    new = random.choice(ch)
    password += new
for j in range(1, sym+1):
    new = random.choice(symbol)
    password += new
for k in range(1, number+1):
    new = random.choice(nu)
    password += new
print(password)















