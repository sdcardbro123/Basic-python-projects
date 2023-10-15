def sieve_eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while p**2 <= n:
        if primes[p]:
            for i in range(p**2, n + 1, p):
                primes[i] = False
        p += 1

    prime_numbers = []
    for i in range(2, n + 1):
        if primes[i]:
            prime_numbers.append(i)

    return prime_numbers

n = 100
prime_numbers = sieve_eratosthenes(n)

twin_primes = []

for i in range(1, len(prime_numbers) - 1):
    if prime_numbers[i + 1] - prime_numbers[i] == 2:
        twin_primes.append((prime_numbers[i], prime_numbers[i + 1]))

print("Twin Primes:")
for twin_prime in twin_primes:
    print(twin_prime)