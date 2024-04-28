file1 = open("example.txt","a")
file1.write("\nNew Sentence")
file1.close()


file2 = open("example.txt" , "r")
print(file2.read())
file2.close()