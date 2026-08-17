# Numpy => Numerical Python used to perform mathematical operations
# Vector Database => Array of Numbers

# Scalar - 12

# vector - 1D array - a -> [0.1, 0.2, 0.3,0.4] * 5

# matrix -> 2D Array - row, columns

# Tensors -> multi 2d array

lst = [10, 20, 30, 40]
[ele*2 for ele in lst]

import array
my_arr = array.array('i', [1, 2, 3, 4, 5])
print(my_arr, type(my_arr))
print(my_arr*2)

import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
arr1*2
print(arr1)

# 1. Lists are highly flexible. -
# 2. Arrays provide better performance - Collection of homogeneous data

# List - Heterogeneous, Array - homogeneous
# List - Less Effiecient, Arrays - Efficient
# List - Slow in mathematical operations, Arrays - faster in mathematical operations(vectorized)

# Limitation of the array is - it works with one dimensional array only
# Numpy allows you to work with multidimensional array

# Pandas, Scikitlearn, Matplotlib, seaborn, tensorflow - Numpy


# Creating an array out of list from homogeneous elements
arr = np.array([10, 20, 30, 40, 50])
print(arr, type(arr))

# ndarray - Multidimensional array

# Array is a collection of homogeneous elements
print(arr.dtype)       # # What kind of data you have inside the array

arr1 = np.array([10.0, 20, 30, 40, 50])
print(arr1, type(arr1))

# Type of elements of the array
print(arr1.dtype)

arr1.shape

# Size of an array - total no of elements inside the array
print(arr1.size)

# Dimension of the array    - Gives te number of dimension of the array
print(arr1.ndim)

# Number of bytes taken by array to store all elements in the array
arr.nbytes

# Upcasting
# Object
# String
# Complex
# Float
# int

# Creating an array with heterogeneous elements
arr2 = np.array([10,20,30,40,50, 60.70, 80+90j])
print(arr2)
print(arr2.dtype)


# Creating an array with heterogeneous elements
arr4 = np.array([10,20,30,40,50, 60.70, 80+90j, '100', [110, 20]], dtype = object)
print(arr4)
print(arr4.dtype)

# VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences
#  (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes)
#  is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray.

# Creating 2D array
arr5 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
arr5
print(arr5)


# Functions to create an array
# arange(start, stop, step)
# Arange can take a fractional value as step whereas range can take only integer value

arr1 = np.arange(10, 21)
arr1


# I want to generate an array of 100 numbers in the same range?
# linspace(start, stop, no_of_elements)
# Stop is inclusive
arr2 = np.linspace(10, 21, 100)
arr2


# Changing the shape of an array
# Random.randint(val1, val2, no_of )
arr1 = np.random.randint(10, 70, 70)
arr1

# Flattening of the array - Converting higher dimension array into single dinemnsion - ravel()
arr1

# Transpose of an array - rows to columns and vice versa
arr2.shape = (10, 10)
arr2

# Arithmetic Operators on array perfomrs the operation elementwise
arr1 = np.random.randint(10, 20, 10)
print(arr1)


# Mathematical Operations   
print(arr1+5)
print(arr1-5)
print(arr1*5)
print(arr1/5)
print(arr1//5)
print(arr1%5)
print(arr1**5)



# Comparison operations
print(arr1>5)
print(arr1<5)
print(arr1<=5)
print(arr1>=5)
print(arr1==5)
print(arr1!=5)
print(arr1&5)


# To perform these operation on the array, the dimension and shape of the array should remain same

arr1 = np.random.randint(10, 50, 5)
arr2 = np.random.randint(10, 90, 6)
print(arr1)
print(arr2)


# Arithmetic operations - element wise
print(arr2+arr1)
print(arr2-arr1)
print(arr2*arr1)
print(arr2/arr1)
print(arr2//arr1)
print(arr2%arr1)
print(arr2**arr1)

print(arr1 > arr2)
print(arr1 < arr2)
print(arr1 >= arr2)
print(arr1 <= arr2)
print(arr1 == arr2)
print(arr1 != arr2)
print(arr1 & arr2)


# Vector product(dot product) - np.dot(arr1, arr2)
# No of elements in both the array shgould be same
print(arr1)
print()
print(arr2)

np.dot(arr1, arr2)


### Understanding Operations on 2D Array
arr1 = np.random.randint(10, 30, 50).reshape(10, 5)
arr1

arr1 = np.random.randint(10, 30, 50).reshape(10, 5)
arr1

arr1+arr2

arr1 -= arr2       # arr1 = arr1-arr2
arr1

arr1 <= arr2

# Unary operations on array - max, min, sum
print(np.max(arr1))

print(np.min(arr1))

print(np.sum(arr1))

np.mean(arr1)

np.max(arr1, axis = 0)     # axis = 0 means find the max

np.max(arr1, axis = 1)



# Indexing and Slicing
arr1 = np.random.randint(10, 20, 10)
arr1

print(arr1[0])
print(arr1[-1])
print(arr1[3:4])

print(arr1[5:1:-1])

arr1 = np.random.randint(10, 20, 30).reshape(5, 6)
print(arr1)

print(arr1[1, 1])
print(arr1[1][1])

print(arr1[::, ::])

print(arr1[::])

print(arr1)

arr1[0]

arr1[::, 0]
print(arr1[1:3])
print(arr1[1:3, ::])

print(arr1[::, 1:3])

print(arr1[1:3, 1:3])
print(arr1[2:, 3:])
print(arr1[1:4:2, 1:4:2])

res = arr1[1, 2], arr1[2, 2], arr1[1, 5], arr1[4, 5]
print(res, type(res))

row_ind = [1, 2, 1, 4]
col_ind = [2, 2, 5, 5]
arr1[row_ind, col_ind]


fruit = np.array([["Banana","Mango","Guava","Avacado"],
            ["Papaya","Jack fruit","Plum","Strawberry"],
            ["Apricot","Apple","Blue berry","Black berry"]])

fruit

# (0, 1), (1, 1), (1, 3), (2, 2) -> 'Potato'

row_ind = [0,1,1,2]
col_ind = [1, 1, 3, 2]
fruit[row_ind, col_ind] = 'Potato'
fruit