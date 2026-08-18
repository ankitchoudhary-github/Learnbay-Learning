# Numpy Methods
import numpy as np

arr1 = np.random.randint(10, 30, 30).reshape(5, 6)
arr1

arr1[1, 2]

arr1 = np.random.randint(10, 30, 30).reshape(5, 6 )
arr1

arr1 < 15

# Accesing all the elements from arr1 which are greater than 15
arr1[arr1 > 15]

np.sum(arr1[arr1 > 15])

np.mean(arr1[arr1 > 15])

# the row and col index positions of all the values which are greater than 15
row, col = np.where(arr1>15)
print(row)
print(col)

arr1[row, col]


# If all elements are mnore than 15 then returns True else if any one elements is less than 15 then it will retyrn False
print(np.all(arr1 > 15))
print(np.all(arr1 >= 10))


# It will returnn True if at least one element is saTUSFYING THE CoND ELSE RETURNS FALSE
print(np.any(arr1 <= 30))
print(np.any(arr1 > 30))

# Iterating over 1-D array
arr1 = np.random.randint(10, 30, 10)
arr1

for ele in arr1:
  print(ele)

# Iterating over 2-D arra

arr2 = np.random.randint(10, 30, 20).reshape(4, 5)
arr2


for ele in arr2:
  print(ele, type(ele))

for row in arr2:
  for ele in row:
    print(ele)

# np.nditer(arr, order = 'C') -> Iteration will happen row-wise
# np.nditer(arr, order = 'F') -> Iteration will happen col-wise

for ele in np.nditer(arr2, order = 'C'):
  print(ele)


for ele in np.nditer(arr2, order = 'F'):
  print(ele)


# Splitting an Array
arr1 = np.random.randint(10, 50, 12)
arr1

# np.split(arr, no_of_splits)
# Note, While splitting, if you are passsing no_of_split as second arg then it should be a factor of no of elements inside the array

arr21, arr22 = np.split(arr1, 2)
print(arr21, arr22)
arr1

np.split(arr1, 4)

# np.split(arr, an iterable of indexes from where you want the split ot happen)
np.split(arr1, [2, 5, 9])



# Splitting 2D array
arr1 = np.random.randint(10, 50, 36).reshape(6, 6)
arr1

np.split(arr1, 2, axis = 0)     # Default split is along axis = 0

np.split(arr1, 2, axis = 1)

a1, a2, a3 = np.split(arr1, [1, 3], axis = 0)
print(a1)



# Concatenation

# 1. If all array are of same shape and size
# 2. along the col if no of rows in all the arrays are same
# 3. along the row if no of col in all the arrays are same

arr1 = np.random.randint(10, 50, 5)
arr1

arr2 = np.random.randint(10, 50, 6)
arr2

np.concatenate((arr1, arr2))

arr1 = np.random.randint(10, 50, 15).reshape(5, 3)
arr1

arr2 = np.random.randint(10, 50, 6).reshape(2, 3)
arr2

np.concatenate((arr1, arr2))   # Default cocatenation is along axis = 0


# Few Important functions
arr1 = np.random.randint(1000, 10000000, 49)
arr1

print(np.max(arr1))

# index of max value in arr1
print(np.argmax(arr1))

# index of min value in arr1
np.argmin(arr1)

# Method to get the index which will sort array1
arr1[np.argsort(arr1)]

arr1[np.where(arr1 > 5000000)]

# view and copy method
#   - view of an array shares the same address of existing array object, so making any changes to view of an array will make changes to original array, Slicing is one of the way to create the view of an array
#   - copy of an array creates a new array apart from  existing array object, so making any changes to copy of an array will not make any changes to original array, we have copy method to create a copy of the array

arr1 = np.random.randint(10, 70, 30)
arr1

arr2 = arr1.reshape(5, 6)
arr2

arr1.shape = (6, 5)
arr1

# Creating view of arr1 - slicing
v1 = arr1[::]
v1

# Understaing copy
arr1 = np.arange(10, 20)
arr1




# Image manipulation using numpy
# Converting image to array

# img_arr = np.array(img)
# img_arr

# #Get the image from the array
# plt.imshow(img_arr)



# ######################################################## HOMEWORK QUESTIONS #################################################################################################

# Why No company is able to build their own LLM?
# What is embedding?
# WHy LLM is called a token Predictor?
# Difference between Fine tuning and RAG.
# Why Prompt and context engineering is important for AI engineers?
#  Job role of an AI engineer
# Difference between AI and ML Engineer
# CPU vs GPU

