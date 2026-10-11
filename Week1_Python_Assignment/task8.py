
name = input("Enter your name: ")
college = input("Enter your college name: ")
branch = input("Enter your branch: ")

# Write information into a text file
with open("introduction.txt", "w") as file:
    file.write("Student Introduction\n")
    file.write("Name: " + name + "\n")
    file.write("College: " + college + "\n")
    file.write("Branch: " + branch + "\n")

print("Introduction saved successfully.")

# Read and display the file contents
with open("introduction.txt", "r") as file:
    content = file.read()

print("\nFile Contents:")
print(content)
