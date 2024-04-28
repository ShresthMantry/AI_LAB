with open('example.txt', 'w') as file:
    file.write("Hello, this is an example text file!\n")
    file.write("You can read this content using Python.")


with open('example.txt', 'r') as file:
    file_content = file.read()


print(file_content)
