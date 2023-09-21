# Create a list
data = [10, 'five', 22, 'three', 100, 'nine', 87, 351]
# Create a lambda function to find the type of the element in the data list
# Map the elements type and save in the result variable
result = map(lambda n: type(n), data)
# Print the saved data in list
print(list(result))
