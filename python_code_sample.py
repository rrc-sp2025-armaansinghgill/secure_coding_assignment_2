"""Module 02 Assignment"""

__author__ = "Armaan Singh Gill"
__version__ = "1.0.0"


# SIMPLE DATA TYPES


# Declared a variable to store name
name = "Armaan"
print("name:", name, "type:", type(name))

# Declared a variable to store status of Manitoba's driving license
license_status = False
print("has license:", license_status, "type:", type(license_status))

# Declared a variable to store the value of current year
current_year = 2025
print("this year:", current_year, "type:", type(current_year)) 

# Increased the value of current year by 1
current_year += 1
print("next year:", current_year, "type:", type(current_year))


# MATHEMATICAL OPERATIONS


# Declared value of Tax Rates as constants
GST = 0.05
PST = 0.07

# Declared a variable to store vehicle purchase price
vehicle_price = 80000.00

# Declared two separate variables to calculate Tax on vehicle
federal_tax = vehicle_price * GST
provincial_tax = vehicle_price * PST

# Declared a variable and Calculated the final cost of the vehicle
final_price = vehicle_price + federal_tax + provincial_tax
print("Purchase price:", vehicle_price, "Provincial Tax:", provincial_tax, "Federal Tax:", federal_tax, "Total:", final_price)

# Printed the above statement in formatted way
print(f"Purchase Price: ${vehicle_price:,.2f} Provincial Tax: ${provincial_tax:,.2f} Federal Tax: ${federal_tax:,.2f} Total: ${final_price:,.2f}")


# LISTS

# Assigned the variable a new list
numbers = [1,2,3,4,5,6,7,8,9,10] 

# Verification of data type
print("type:", type(numbers))

print("list:", numbers)

# Adding first name between the elements
numbers.insert(5,"Armaan")
print("Updated List:", numbers)

# Removing number 9 from the list
numbers.remove(9)
print("Updated List:", numbers)

# Creating a new list
alphabets = ['A','B','C']

# Declaring a variable that contains value from both lists
final_list = numbers + alphabets
print(final_list)


# TUPLES

# Assigning the variable as a Tuple
provinces = ("Manitoba", "Alberta", "British Columbia", "Ontario")

# Verifying the data type
print("type:", type(provinces))

print("Provinces:", provinces)


# DICTIONARIES

# Declaring a variable to store a dictionary
coins = {"nickel":0.05, "dime":0.10, "quarter":0.25}

# Verifying the data type
print("type:", type(coins))

print("Dictionary:", coins)

# Modifying the values of each item in a dictionary
coins["nickel"] = 5
coins["dime"] = 10
coins["quarter"] = 25

print("Updated Dictionary:", coins)

# Adding Loonie and Toonie to the dictionary
coins["loonie"] = 100
coins["toonie"] = 200

print("Recently Updated Dictionary:", coins)


# SETS

# Declaring a variable to store a set of even numbers
even_numbers = {4,6,8,10,12,14,16,18}

# Verifying data type
print("type:", type(even_numbers))

print("Even Numbers:", even_numbers)

# Declaring a variable to store a set of multiples of 5
multiples_of_five = {10,15}
print("Multiples of 5:", multiples_of_five)

# Declaring a variable to store a set of unique values of two sets created above
combined_set = even_numbers.union(multiples_of_five)
print("Combined Set", combined_set)

# Declaring a variable to store a set of common values of two sets created above
common_value = even_numbers.intersection(multiples_of_five)
print("Common value Set:", common_value)

# Declaring a variable to store a set which contains only the values that appear in first set but not in second set
new_set = even_numbers.difference(multiples_of_five)
print("Exclusive even numbers:", new_set)

# Declaring a variable to store a set which contains only the values that appear in second set but not in first set
new_set_1  = multiples_of_five.difference(even_numbers)
print("Exclusive multiple of 5:", new_set_1)




