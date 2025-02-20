# Writing to a file
with open("my_file.txt", "w") as f:
    f.write("This is some text.\n")
    f.write("More text on a new line.\n")

# Reading from a file
with open("my_file.txt", "r") as f:
    content = f.read()
    print("File content:\n", content)

# Appending to a file
with open("my_file.txt", "a") as f:
    f.write("This is appended text.\n")
