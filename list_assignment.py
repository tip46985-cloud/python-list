# ------------------------------------------
# 1. Python List Transformation
# ------------------------------------------

print("---- Part 1: Python List Transformation ----")

# Task 1: Sort grades in descending order
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades_sorted_desc = sorted(grades, reverse=True)
print("Sorted grades (descending):", grades_sorted_desc)

# Task 2: Calculate the average grade
average_grade = sum(grades) / len(grades)
print("Average grade:", average_grade)

# ------------------------------------------
# 2. Advanced List Methods and Identity Operators
# ------------------------------------------

print("\n---- Part 2: List Methods & Identity Operators ----")

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

# Task: Check if Alice submitted and attended
if "Alice" in submitted and "Alice" in attended:
    print("Alice submitted her assignment and attended class.")
else:
    print("Alice did not both submit and attend.")

# ------------------------------------------
# 3. Advanced Slicing Techniques
# ------------------------------------------

print("\n---- Part 3: Advanced Slicing ----")

temperatures = [
    72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90,
    91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106
]

# Task 1: Extract second week temperatures (index 7 to 13 inclusive)
second_week = temperatures[7:14]
print("Second week temperatures:", second_week)

# Task 2: Extract temperatures above 100
temps_above_100 = [temp for temp in temperatures if temp > 100]
print("Temperatures above 100:", temps_above_100)
