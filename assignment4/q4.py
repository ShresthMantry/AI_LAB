def find_maximums(list1, list2):
    if len(list1) != len(list2):
        return "Error: Lists must be of the same size"

    max_list = []
    for i in range(len(list1)):
        max_list.append(max(list1[i], list2[i]))
    
    return max_list

n = int(input("Enter number of elements : "))
lst1 = list(map(int, 
    input("\nEnter the numbers : ").strip().split()))[:n]

lst2 = list(map(int, 
    input("\nEnter the numbers : ").strip().split()))[:n]

max_elements = find_maximums(lst1, lst2)
print("Maximum elements between corresponding elements of the two lists:", max_elements)
