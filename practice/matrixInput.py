n = int(input("Enter a number"))
m= int(input("Enter a number"))
arr=[]


for i in range(n):
    col=[]
    for j in range (m):
        col.append(int(input()))
    arr.append(col)   


# arr = list(map(int,input().strip().split()))[:n]

print(arr[1][1])