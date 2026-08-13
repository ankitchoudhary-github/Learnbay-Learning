# String Length Using Built-in Function
# Success rate: 14.65%
# Write a Python program that reads a single line of text from standard input and prints the number of characters in that text. Use Python’s built-in len() function rather than manually iterating through each character.

# Input:
# A single line of text (which may include letters, digits, symbols, spaces, or even be empty).

# Output:
# A single integer representing the length of the input text.

# Example:

# Input:
# Write a Python program to find the length of the my_str

# Output:
# 55

my_str=input()
print(len(my_str))








# Counting Lowercase 'p' Occurrences
# Success rate: 23.14%
# Write a Python program that reads a single line of text from standard input (STDIN) and prints the number of times the lowercase letter p appears in that line. Your solution should use Python’s built-in string methods.

# Input Format:
# A single line of text.

# Output Format:
# An integer representing the count of lowercase p characters.

# Example

# Input:
# peter piper picked a peck of pickled peppers.

# Output:
# 9

str=input()
print(str.count('p'))







# Counting Lowercase 'p' Occurrences
# Success rate: 23.14%
# Write a Python program that reads a single line of text from standard input (STDIN) and prints the number of times the lowercase letter p appears in that line. Your solution should use Python’s built-in string methods.

# Input Format:
# A single line of text.

# Output Format:
# An integer representing the count of lowercase p characters.

# Example

# Input:

# peter piper picked a peck of pickled peppers.

# Output:
# 9

str=input()
print(str.count('p'))








# Find All Indices of Lowercase 'p' in a String
# Write a Python program that reads a single string from standard input and prints the zero-based indices of every occurrence of the lowercase letter 'p'. You should use a built-in function or idiomatic Python (for example, using str.find() repeatedly, or enumerate in a list comprehension) rather than manual character-by-character indexing.

# Input Format
# A single line containing the string S.

# Output Format
# Print each index where S[i] == 'p' on its own line, in ascending order. If there are no 'p's in the string, print nothing.

# Constraints

# 1 ≤ |S| ≤ 10^5
# S may include lowercase letters, spaces, punctuation, etc.

text = input()
for index, char in enumerate(text):
    if char == 'p':
        print(index)







# Split a Sentence into Words
# Success rate: 59.73%
# Write a Python program that reads a single line of text from standard input and uses the built-in str.split() method to divide it into individual words. The program should then print the resulting list of words in Python list format.

# You should not implement your own parsing logic; simply call split() without arguments, which splits on any whitespace.
# Punctuation remains attached to the word it follows.
# If the input is empty or contains only whitespace, print an empty list ([]).
# Input
# A single line of text (which may include letters, digits, punctuation, and spaces).

# Output
# A Python list of words (as a string) in the order they appear in the sentence. The program will be evaluated against 5 test cases.

# Example
# Input:

# peter piper picked a peck of pickled peppers.
# Output:

# ['peter', 'piper', 'picked', 'a', 'peck', 'of', 'pickled', 'peppers.']

str= input()
words= str.split()
print (words)








# Reverse Word Order in a Sentence
# Write a Python program that reads a single line (a sentence) from standard input, reverses the order of its words using built-in methods, and prints the resulting sentence.

# Treat any contiguous sequence of non-space characters as one word (including punctuation).
# Preserve punctuation attached to words.
# Separate words in the output by a single space, with no leading or trailing spaces.

str= input()
words= str.split()
print("".join(words[::-1]))








# Reverse Word Order
# Success rate: 29.03%
# Write a program that reads a line of text from standard input, splits it into words, reverses the order of those words, and prints the result as a single line. Punctuation and capitalization should be treated as part of the word.

# Input Format
# A single line containing zero or more words (possibly including punctuation).

# Output Format
# A single line containing the original words in reverse order, separated by single spaces.
s = input()
words = s.split()
print(" ".join(words[::-1]))









# Reverse a String
# Success rate: 27.63%
# Write a program that reads a line of text from standard input and prints its characters in reverse order.

# Reversing a string is a common exercise in many coding interviews and helps reinforce working with indices and slicing.
s = input()

i = len(s) - 1

while i >= 0:
    print(s[i], end="")
    i -= 1







# Reverse Each Word in a Sentence (Using Built-in Functions)
# Problem Statement
# Given a sentence S, write a Python program that reverses each word in S using Python's built-in functions, while preserving the original word order and spaces.

# Input Format
# A single line containing the string S.

# Output Format
# A single line containing the transformed sentence, where each word's characters are reversed.

# Instructions
# Implement your solution in Python. You are encouraged to use built-in functions such as split(), string slicing (e.g., word[::-1]), reversed(), and join() to achieve a concise and efficient solution.

# Constraints
# 1 ≤ length of S ≤ 10^5
# S consists of printable ASCII characters (letters, digits, punctuation) and spaces
# There is no leading or trailing space, and words are separated by a single space
s = input()

words = s.split()

for i in range(len(words)):
    words[i] = words[i][::-1]

print(" ".join(words))






# Title Case a Sentence
# Success rate: 26.03%
# Write a Python program that reads a single line of text and converts it so that the first character of each word is uppercase and the remaining characters are lowercase. You should leverage Python's built-in string methods (for example, str.title() or a combination of str.split() and str.capitalize()).

# Input Format

# A single line containing a sentence. The sentence may include letters, digits, punctuation, and spaces.
# Output Format

# Print the transformed sentence in title case.
# Sample

# Input:

# peter piper picked a peck of pickled peppers.

# Output:

# Peter Piper Picked A Peck Of Pickled Peppers.
# Your solution should run correctly on 5 test cases, covering typical, edge, and empty inputs.

# Feel free to use any built-in string methods to achieve the result.

s = input()
print(s.title())







# Sentence Case Conversion
# Success rate: 65.09%
# In this exercise, you’ll write a Python program that reads a line of text from standard input and prints it back in sentence case: the first character should be uppercase and all other letters should be lowercase. You should use only Python’s built-in string methods (e.g. str.lower(), str.capitalize(), etc.) to accomplish this.

# Input Format
# A single line containing a non-empty sentence. The sentence may include letters, spaces, and punctuation.

# Output Format
# A single line containing the same sentence converted to sentence case.

# Sample Input

# Peter Piper Picked A Peck Of Pickled Peppers.
# Sample Output

# Peter piper picked a peck of pickled peppers.
# Your solution will be tested against five test cases.

s = input()

print(s.capitalize())






# Sentence Normalizer
# Write a Python program that reads a single line of text from standard input and transforms 
# it so that only the very first character of the entire string is uppercase, and all other alphabetic characters are lowercase. 
# Non‐alphabetic characters (spaces, punctuation, digits) should remain in their original positions.

s = input()

print(s.capitalize())







# String Index Finder (using built-in)
# Success rate: 53.88%
# In this exercise you’ll write a Python program that finds the first occurrence of a substring inside a given string, using Python’s built-in string methods.

# Example:

# Input:
# Peter Piper Picked A Peck Of Pickled Peppers.
# Pickl

# Output:
# 29
# Your solution will be tested on 5 test cases.

# Given two lines of input:

# Line 1: my_str – the text in which we’ll search
# Line 2: sub_str – the pattern we want to find
# Your program should print the zero-based index of the first character of the first match. If sub_str does not occur in my_str, print -1.

# You must use one of Python’s built-in string search methods (for example, str.find() or str.index() with exception handling).

my_str = input()
sub_str = input()

print(my_str.find(sub_str))







# First Occurrence Replacement
# Success rate: 25.81%
# You are given three lines of input:

# my_str (the original string)
# sub_str (the substring to find)
# new_str (the substring to replace it with)
# Write a Python program that:

# Replaces only the first occurrence of sub_str in my_str with new_str.
# Prints the resulting string if the replacement was made.
# If sub_str is not found in my_str, prints:
# [sub_str] not found
# where you output the actual value of sub_str followed by the phrase "not found".

# You should use Python’s built-in str.replace() method with the optional count argument.

my_str = input()
sub_str = input()
new_str = input()

if sub_str in my_str:
    print(my_str.replace(sub_str, new_str, 1))
else:
    print(sub_str, "not found")







# Centered Substring Formatter
# Success rate: 15.57%
# Problem
# In text formatting, it’s common to align or center a piece of text within a fixed-width field, filling the unused space with a padding character. Python provides built-in methods such as str.center, str.rjust, and str.ljust to help with these tasks.

# Write a program that takes:

# A string S (the field)
# A substring T
# and outputs a new string of the same length as S in which:

# The substring T appears exactly centered.
# All other positions are filled with the asterisk character (*).
# If the number of padding characters is odd, place the extra padding character on the left side.

# You must use Python’s built-in string formatting methods (for example, str.center or a combination of rjust/ljust) to implement your solution.


s = input()
t = input()

print(t.center(len(s), "*"))









# *********************END********************