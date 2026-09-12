# Open file in write mode
file = open("my_data.txt", "w")
file.write("This is my first persistent data!")
file.close()

print("Data saved successfully.")

# Open file in read mode
file = open("my_data.txt", "r")
content = file.read()
file.close()

print("File content:", content)


##################

with open("user_info.txt", "w") as file:
    file.write("my name is amir.")

with open("user_info.txt", "r") as file:
    content = file.read()
print("file content:", content)

##################
with open("user_info.txt", "a") as file:
    file.write("\nI am learning Python.")

with open("user_info.txt", "r") as file:
    content = file.read()
print("file content:", content)
##################

with open("user_info.txt", "a") as file:
    file.write("\nThis is my new exercise.")
with open("user_info.txt", "r") as file:
    content = file.read()
print("file content:", content)
