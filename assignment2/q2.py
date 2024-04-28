def read_characters_from_file(filename, num_characters):
    with open(filename, 'r') as file:
        content = file.read(num_characters)
    return content

num_characters_to_read = 10

file_content = read_characters_from_file('example.txt', num_characters_to_read)

print(file_content)
