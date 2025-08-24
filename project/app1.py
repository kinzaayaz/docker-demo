# Step 1: Take user input
user_name = input("Enter your name: ")

# Step 2: Save the name in the file (append mode so old data is not lost)
with open("user_info.txt", "a") as file:
    file.write(user_name + "\n")

# Step 3: Ask if user wants to see all names
choice = input("Would you like to see the list of all names? (y/n): ")

if choice.lower() == "y":
    with open("user_info.txt", "r") as file:
        names = file.readlines()
        for name in names:
            print(name.strip())
else:
    print("Okay, have a nice day!")


