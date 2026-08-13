
# inp_str = 'peter piper picked a peck of pickled peppers'
# # output2:- 'retep repip dekcip a kcep fo delkcip sreppep'
inp_str = "peter piper picked a peck of pickled peppers"

i = 0
word = ""
while i < len(inp_str):

    if inp_str[i] != " ":
        word += inp_str[i]
    else:
        j = len(word) - 1
        while j >= 0:
            print(word[j], end="")
            j -= 1
        print(end=" ")
        word = ""
    i += 1
j = len(word) - 1
while j >= 0:
    print(word[j], end="")
    j -= 1


# Homework
# Que 1 :- Create a program that simulates an ATM login. The user has a maximum of 3 attempts to enter the correct PIN (e.g., 1234).
# If the user enters the correct PIN, print "Access Granted" and break the loop.
# If they enter the wrong PIN, print "Incorrect PIN. Attempts remaining: X" and continue to the next attempt.
# If they fail 3 times, print "Account Locked."

correct_pin = '1234'
attempts = 3

while attempts > 0:
  user_inp = input(f'Enter the correct PIN ({attempts} remaining):')
  if user_inp == correct_pin:
    print('Access Granted')
    break
  attempts -= 1
  if attempts > 0:
    print(f' You have entered an incorrect PIN. Attempts Remaining {attempts}')
  else:
    print('Account is Locked!!!')







# Que 2: Create a shopping list builder where  he user can type in items.
# If the item is already in the list, print "Item already exists" and continue without adding it.
# If the user types "done", break the loop and print the final alphabetized list.
# Constraint: If the user enters a number instead of a string (e.g., "5" instead of "Apples"), use isdigit() to check; print "Invalid input" and continue.

shopping_list = []

while True:
    item = input("Enter item: ").strip()

    if item.lower() == 'done':
        break

    if item.isdigit():
        print("Invalid input . Please enter an item and not a number")
        continue

    if item in shopping_list:
        print("Item already exists")
        continue

    if item.lower() in shopping_list:
       print(f'{item} is already existing ! ! !')
       continue

if item:
   shopping_list+=[item.lower()]
   print(f"{item} is Added")

print('\n Shopping List Items are as below: \n')

for items in shopping_list:
   print (items)






# Que 3: Write a program that asks the user to input numbers one by one.
# The program should keep a running total (sum) of the numbers.
# If the user enters a number that is a multiple of 5, it should not be added to the sum (continue).
# If the user enters a negative number, the loop should end (break).
# Finally, print the total sum.

total_sum = 0

while True:
    num = int(input("Enter a number, -ve to end : "))

    if num < 0:
        print("Negative Number entered. Ending the Program")
        break

    if num % 5 == 0:
        print(f"Skipping {num} as it is a multiple of 5")
        continue

    total_sum += num

print("Total Sum =", total_sum)








# Que 4: Write a script that asks the user for a starting number and then finds the next 5 prime numbers after that value.
# Use a while loop to keep searching until you find exactly 5 primes.
# Use a nested loop to check if a number is prime.
# Use break to stop checking a number once you find a divisor, and use continue or a counter to keep track of how many primes you have found.


import math
num = int(input('Enter a number to check whether it is prime or not?: '))
start_num_divisible = 2
check_till = math.floor(math.sqrt(num))
while start_num_divisible <= check_till:
  if num % start_num_divisible== 0:
    print(f'{num} is divisible by {start_num_divisible}. So not a prime Number.')
    break
  else:
    start_num_divisible+=1
else:
  print(f"{num} is a prime number")