import math

# 素数列挙
def prime_numbers(x: int) -> list:
	if x < 2:
		return []

	prime_numbers = [i for i in range(x)]
	prime_numbers[1] = 0

	for prime_number in prime_numbers:
		if prime_number > math.sqrt(x):
			break

		if prime_number == 0:
			continue

		for composite_number in range(2 * prime_number, x, prime_number):
			prime_numbers[composite_number] = 0

	return [prime_number for prime_number in prime_numbers if prime_number != 0]
	
# 素数判定
def is_prime(x: int) -> bool:
	if x < 2: return False
	if x == 2 or x == 3 or x == 5: return True
	if x % 2 == 0 or x % 3 == 0 or x % 5 == 0: return False

	prime_number = 7
	difference = 4

	while prime_number <= math.sqrt(x):
		if x % prime_number == 0: return False

		prime_number += difference
		difference = 6 - difference

	return True

# 素因数分解
def prime_factorize(n: int) -> list:
	res = []

	while n % 2 == 0:
		res.append(2)
		n //= 2

	f = 3

	while f ** 2 <= n:
		if n % f == 0:
			res.append(f)
			n //= f
		else:
			f += 2

	if n != 1:
		res.append(n)

	return res