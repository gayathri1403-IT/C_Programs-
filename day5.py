# Day 5: Basic List Operations

# Step 1: Create a list
numbers = [12, 5, 7, 25, 18]

print("Original List:", numbers)

# Step 2: Add an element to the list
numbers.append(30)
print("After Adding 30:", numbers)

# Step 3: Remove an element from the list
numbers.remove(7)
print("After Removing 7:", numbers)

# Step 4: Sort the list
numbers.sort()
print("Sorted List:", numbers)

# Step 5: Find maximum and minimum values
print("Maximum Value:", max(numbers))
print("Minimum Value:", min(numbers))

# Step 6: Print all elements using a loop
print("List Elements (using loop):")
for num in numbers:
    print(num)