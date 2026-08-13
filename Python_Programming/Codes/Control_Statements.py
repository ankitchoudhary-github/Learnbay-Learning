# Write a Python program that:

# Reads a single integer N from standard input.
# If N is between 0 and 9 inclusive, prints its English word equivalent in lowercase (e.g. "zero", "one", …, "nine").
# Otherwise, prints the message:
# "{N} is outside of the range"
# Exit immediately after printing.

n = int(input())

if n == 0:
    print("zero")
elif n == 1:
    print("one")
elif n == 2:
    print("two")
elif n == 3:
    print("three")
elif n == 4:
    print("four")
elif n == 5:
    print("five")
elif n == 6:
    print("six")
elif n == 7:
    print("seven")
elif n == 8:
    print("eight")
elif n == 9:
    print("nine")
else:
    print(n, "is outside of the range")


