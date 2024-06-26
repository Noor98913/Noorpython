def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes_up_to_number(number: int) -> int:
    count = 0
    for i in range(2, number + 1):
        if is_prime(i):
            count += 1
    return count

# Prompt user to enter a number
user_input = int(input("Enter a number: "))

# Count the number of prime numbers up to the entered number
prime_count = count_primes_up_to_number(user_input)

print(f"The number of prime numbers up to {user_input} is: {prime_count}")