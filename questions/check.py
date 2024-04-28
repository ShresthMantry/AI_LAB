# def uniquewordsandfreq(content):
# 	frequency = {}
# 	for word in content:
# 		frequency[word] = 0

#     for word in content:
#         frequency[word]=frequency[word]+1

# 	print("Unique words")
# 	print(len(frequency))
# 	print(frequency)

def uniquewordsandfreq(content):
    frequency = {}
    for word in content:
        frequency[word]=0

    for word in content:
        frequency[word]=frequency[word]+1

    print("Unique words")
    print(len(frequency))
    print(frequency)
		


