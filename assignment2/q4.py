count = 0;
file = open("file.txt","r")
for line in file:
    if not line.strip().startswith('T'):
        count=count+1

print(count)
        
