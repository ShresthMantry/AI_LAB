f1 = open("a1.txt",'r')
countwords = 0
countlines = 0
countspaces = 0
content = f1.read()
contentcopy = content
content = content.strip().split()
print("Total Words")
print(len(content))

frequency = {}
for word in content:
        frequency[word] = 0

for word in content:
        frequency[word]=frequency[word]+1


print("Unique words")
print(len(frequency))
print(frequency)


maxlen = -1
maxword = ""
total = 0

for word in frequency:
        total = total + len(word)
        if len(word)>maxlen:
                maxlen = len(word)
                maxword = word


print("max len and max word")
print(maxlen)
print(maxword)

print("Average Length")
avg = total/len(content)
print(avg)


def compareText(a,b):
        if a.equals(b):
                return True
        else :
                return False