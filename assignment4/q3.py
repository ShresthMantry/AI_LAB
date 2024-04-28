def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def count_numbers(lst):
    odd_count = 0
    even_count = 0
    prime_count = 0
    non_prime_count = 0

    for num in lst:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        if is_prime(num):
            prime_count += 1
        else:
            non_prime_count += 1

    return odd_count, even_count, prime_count, non_prime_count


n = int(input("Enter number of elements : "))
lst = list(map(int, 
    input("\nEnter the numbers : ").strip().split()))[:n]
odd, even, prime, non_prime = count_numbers(lst)

print(f"Number of odd numbers: {odd}")
print(f"Number of even numbers: {even}")
print(f"Number of prime numbers: {prime}")
print(f"Number of non-prime numbers: {non_prime}")
