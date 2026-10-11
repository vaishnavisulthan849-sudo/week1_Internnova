
# 1. String operations
text = "Python Programming"

print("Original:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Replace:", text.replace("Python", "Data"))
print("Position of Programming:", text.find("Programming"))

# 2. List operations
numbers = [40, 10, 30, 20]

numbers.append(50)
print("\nAfter append:", numbers)

numbers.remove(10)
print("After remove:", numbers)

numbers.sort()
print("After sort:", numbers)

# 3. Tuple creation and indexing
fruits = ("Apple", "Banana", "Mango")

print("\nTuple:", fruits)
print("First fruit:", fruits[0])
print("Third fruit:", fruits[2])

# 4. Dictionary storing student information
student = {
    "name": "Vaishnavi",
    "branch": "CSE",
    "marks": 85
}

print("\nStudent Information:", student)
print("Student Name:", student["name"])
print("Student Branch:", student["branch"])

# 5. Set operations
colors = {"Red", "Blue", "Green"}

colors.add("Yellow")
print("\nAfter add:", colors)

colors.remove("Blue")
print("After remove:", colors)
