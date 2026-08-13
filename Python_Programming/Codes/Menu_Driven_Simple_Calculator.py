# Menu-Driven Simple Calculator
# Write a Python program using only conditional statements that implements a console-based calculator. Your program should:

# Display the following menu exactly as shown:
# Please select any one operation from below:-
# * To add enter 1
# * to subtract enter 2
# * To multiply enter 3
# * To divide enter 4
# * To divide and find quotient enter 5
# * To divide and find remainder enter 6
# * To divide and find num1 to the power of num2 enter 7
# * To Come out of the program enter 8
# Read an integer choice from input.
# If choice is between 1 and 7, read two numbers (num1 and num2). Both integers and floats are allowed.
# For choice 1: print num1 + num2.
# For choice 2: print num1 - num2.
# For choice 3: print num1 * num2.
# For choice 4: if num2 is zero, print Error: Division by zero; otherwise compute num1 / num2 and round to two decimal places.
# For choice 5: if num2 is zero, print Error: Division by zero; otherwise print the integer quotient num1 // num2.
# For choice 6: if num2 is zero, print Error: Division by zero; otherwise print the remainder num1 % num2.
# For choice 7: print num1 ** num2.
# If choice is 8, print Exiting program and terminate without reading further input.
# Do NOT define any functions or use exception handling; rely solely on if/elif/else for control flow.

# Input Format (STDIN):

# <choice>
# [num1]
# [num2]
# If <choice> is 1–7, two additional lines follow.
# If <choice> is 8, no further input is provided.
# Output Format (STDOUT):

# First, echo the full menu (8 lines).
# On the next line, print either the computed result, Error: Division by zero, or Exiting program.
# Concepts Covered: Conditional statements, basic I/O, arithmetic operations, rounding with round().

# Sample test cases
# Input
# Expected output
# 1
# 10
# 5
# Please select any one operation from below:-
# * To add enter 1
# * to subtract enter 2
# * To multiply enter 3
# * To divide enter 4
# * To divide and find quotient enter 5
# * To divide and find remainder enter 6
# * To divide and find num1 to the power of num2 enter 7
# * To Come out of the program enter 8
# 15
# 4
# 7
# 2
# Please select any one operation from below:-
# * To add enter 1
# * to subtract enter 2
# * To multiply enter 3
# * To divide enter 4
# * To divide and find quotient enter 5
# * To divide and find remainder enter 6
# * To divide and find num1 to the power of num2 enter 7
# * To Come out of the program enter 8
# 3.5
# 4
# 5
# 0
# Please select any one operation from below:-
# * To add enter 1
# * to subtract enter 2
# * To multiply enter 3
# * To divide enter 4
# * To divide and find quotient enter 5
# * To divide and find remainder enter 6
# * To divide and find num1 to the power of num2 enter 7
# * To Come out of the program enter 8
# Error: Division by zero
# 7
# 2
# 3
# Please select any one operation from below:-
# * To add enter 1
# * to subtract enter 2
# * To multiply enter 3
# * To divide enter 4
# * To divide and find quotient enter 5
# * To divide and find remainder enter 6
# * To divide and find num1 to the power of num2 enter 7
# * To Come out of the program enter 8
# 8
# 8
# Please select any one operation from below:-
# * To add enter 1
# * to subtract enter 2
# * To multiply enter 3
# * To divide enter 4
# * To divide and find quotient enter 5
# * To divide and find remainder enter 6
# * To divide and find num1 to the power of num2 enter 7
# * To Come out of the program enter 8
# Exiting program





print("Please select any one operation from below:-")
print("* To add enter 1")
print("* to subtract enter 2")
print("* To multiply enter 3")
print("* To divide enter 4")
print("* To divide and find quotient enter 5")
print("* To divide and find remainder enter 6")
print("* To divide and find num1 to the power of num2 enter 7")
print("* To Come out of the program enter 8")

choice = int(input())

if choice == 8:
    print("Exiting program")
elif 1 <= choice <= 7:
    num1 = float(input())
    num2 = float(input())

    if choice == 1:
        print(num1 + num2)

    elif choice == 2:
        print(num1 - num2)

    elif choice == 3:
        print(num1 * num2)

    elif choice == 4:
        if num2 == 0:
            print("Error: Division by zero")
        else:
            print(f"{num1 / num2:.2f}")

    elif choice == 5:
        if num2 == 0:
            print("Error: Division by zero")
        else:
            print(int(num1 // num2))

    elif choice == 6:
        if num2 == 0:
            print("Error: Division by zero")
        else:
            print(num1 % num2)

    elif choice == 7:
        print(num1 ** num2)

else:
    print("Invalid Choice")







year = int(input())

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")



num1 = int(input())
num2 = int(input())

if num1 > num2:
    print(num1, "is greater than", num2)
elif num1 < num2:
    print(num1, "is smaller than", num2)
else:
    print(num1, "is equal to", num2)





num1 = int(input())
num2 = int(input())

print(
    "num1 is greater than num2" if num1 > num2
    else "num1 is smaller than num2" if num1 < num2
    else "num1 is equal to num2"
)