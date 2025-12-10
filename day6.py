# Day 6: Functions in Python

# Function to find square of a number
def find_square(n):
    return n * n

# Function to find cube of a number
def find_cube(n):
    return n * n * n

# Main program
num = int(input("Enter a number: "))

print("Square of", num, "=", find_square(num))
print("Cube of", num, "=", find_cube(num))