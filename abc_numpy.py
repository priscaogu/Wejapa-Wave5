#Create a numpy array of strings containing letters 'a' through 'j' (inclusive) of the alphabet. Then, use numpy array attributes to print the following information about this array:

#dtype of array

#shape of array
#size of array

#The code you submit in the code editor below will not be graded. Use the results from your code below, along with what you remember from the previous video, to complete the quiz below the code editor.



import numpy as np

# create numpy array of letters a-j
letter_array = 
print("Letter Array: ", letter_array)

letter_array = np.arange(20)
print("Letter Array: ", letter_array)

# get dtype of array
type = type(letter_array)
print(type)

# get shape of array
shape = letter_array.shape
print(shape)



# get size of array
size = letter_array.size
print(size)