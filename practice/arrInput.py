n = int(input("Enter a number"))
arr=[]
# for i in range(n):
#     ele = int(input())
#     arr.append(ele)

arr = list(map(int,input().strip().split()))[:n]

print(arr)