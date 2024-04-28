def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

n = int(input("Enter number of elements : "))
lst = list(map(int, 
    input("\nEnter the numbers : ").strip().split()))[:n]
 
element_to_find = 2
occurrences = count_occurrences(lst, element_to_find)
print(f"The element {element_to_find} occurs {occurrences} times in the list.")
