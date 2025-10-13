# 1)
# Create a function called "car_at_light"
# It should take one parameter: "light"
# which gives the color of a traffic light.
# If the color is "red", the function should return
# "stop". If the color is "green", the function
# should return "go". If the color is "yellow"
# the function should return "wait". If the color
# is anything else, the function should raise
# an exception with the following message: 
# "Undefined instruction for color: <light>" 
# where <light> is the value of the parameter light.
#

def car_at_light(light):
    if light == "red":
        return "stop"
    elif light == "green":
        return "go"
    elif light == "yellow":
        return "wait"
    else:
        raise Exception(f"Undefined instruction for color: {light}")
    

light_color = car_at_light(input("Enter a color: "))
print(light_color)



# 2)
# Create a function named "safe_subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
# If the values cannot be subtracted due to its type, 
# it returns None.
# If there is any other reason why it fails show the problem 
# 

ejemplo= (1,2,3,4,5)
ejemplo_2=(5,6,7,8)

# 3)
# Imagine you have a dictionary with the attributes of a person
# {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
# {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# create two functions that returns the age of the person
# that handles both examples.
# Name the first function "retrieve_age_eafp" and follow EAFP
# Name the second function "retrieve_age_lbyl" and follow lbyl

# 4)
# Imagine you have a file named data.csv. 
# Create a function called "read_data" that reads the file
# making sure to use to handle the fact 
# that it might not exist. 
#
import pandas as pd

def read_data(filename="data.csv"):
  """
  Reads data from a CSV file, handling FileNotFoundError.

  Args:
    filename: The name of the CSV file to read (default is "data.csv").

  Returns:
    A pandas DataFrame if the file is read successfully, otherwise None.
  """
  try:
    df = pd.read_csv(filename)
    return df
  except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    return None
  except Exception as e:
    print(f"An error occurred while reading the file: {e}")
    return None

# Example usage:
# Assuming 'data.csv' exists in the current directory
# data_df = read_data()
# if data_df is not None:
#   display(data_df.head())

# Example usage with a non-existent file
# non_existent_df = read_data("non_existent_file.csv")

# 5) Squash some bugs! 
# Find the possible logical errors (bugs) 
# in the code blocks below. Comment in each of them
# which logical errors did you find and correct them
### (a)
#
#total_double_sum = 0
#for elem in [10, 5, 2]:
#    double = elem * 2
#    total_double_sum += elem
#

# Logical error: The variable 'total_double_sum' is accumulating the original 'elem' values
# instead of the 'double' values.
total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    # Corrected line: Add 'double' to the total
    total_double_sum += double

### (b)
#strings = ''
#for string in ['I', 'am', 'Groot']:
#    strings = string+"_"+string

# Logical error: The loop is overwriting the 'strings' variable in each iteration
# instead of concatenating the strings. This results in 'strings' only holding
# the result of the last iteration. Also, it concatenates the same string twice.
strings = ''
for string in ['I', 'am', 'Groot']:
    # Corrected line: Concatenate the current string with a space to the existing 'strings'
    strings += string + " "
print(strings)

### (c) Careful!
#j=10
#while j > 0:
#   j += 1

# Logical error: The condition 'j > 0' and the increment 'j += 1' will cause an infinite loop
# because j will always be greater than 0 and will keep increasing.
j=10
# Corrected code: Change the condition or the increment to ensure the loop terminates.
# For example, to loop while j is greater than 0 and decrement j:
while j > 0:
   j -= 1 # Corrected line: Decrement j instead of incrementing
print(f"Corrected loop for (c): j ends at {j}")

# Or, if the intention was to loop a specific number of times while j is positive:
j = 10
for i in range(j): # Loop 10 times
    print(f"Loop iteration {i}, j is {j}")

### (d)
#productory = 0
#for elem in [1, 5, 25]:
#    productory *= elem

# Logical error: The variable 'productory' is initialized to 0. Any multiplication
# by 0 will result in 0, so the productory will remain 0 regardless of the elements
# in the list.
productory = 0
for elem in [1, 5, 25]:
  productory *= elem
print(f"Corrected productory for (d): {productory}")

# Code to multiply each value in the vector by 3
numbers = [1, 5, 25]
result = [elem * 3 for elem in numbers]
print(f"Result of multiplying each element by 0: {result}")