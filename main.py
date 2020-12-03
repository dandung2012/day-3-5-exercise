# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = name1 + name2

letter_T = name.upper().count('T')
letter_R = name.upper().count('R')
letter_U = name.upper().count('U')
letter_E = name.upper().count('E')

letter_L = name.upper().count('L')
letter_O = name.upper().count('O')
letter_V = name.upper().count('V')
letter_EE = name.upper().count('E')

total_true = letter_T + letter_R + letter_U + letter_E
total_love = letter_L + letter_O + letter_V + letter_EE
total1 = str(total_true) + str(total_love)

total = int(total1)
if total < 10 or total > 90:
  print(f'your love score is {total}, you great')
elif total >= 40 and total <= 60:
  print(f'your love score is {total}, you are allright')
else:
  print(f'your love score is {total}')
