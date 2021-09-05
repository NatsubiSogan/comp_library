import random

# mod-sqrt
def mod_sqrt(a: int, p: int) -> int:
	if a == 0: return 0
	if p == 2: return 1
	k = (p - 1) // 2
	if pow(a, k, p) != 1: return -1
	while True:
		n = random.randint(2, p - 1)
		r = (n ** 2 - a) % p
		if r == 0: return n
		if pow(r, k, p) == p - 1: break
	k += 1
	w, x, y, z = n, 1, 1, 0
	while k:
		if k % 2:
			y, z = w * y + r * x * z, x * y + w * z
		w, x = w * w + r * x * x, 2 * w * x
		w %= p; x %= p; y %= p; z %= p
		k >>= 1
	return y