from kth_root_integer import root_ceil

# Baby-Step Giant-Step
def discrete_logarithm(x: int, y: int, m: int) -> int:
	if m == 1: return 0
	if y == 1: return 0
	if x == 0:
		if y == 0: return 1
		else: return -1
	sq = root_ceil(m, 2) + 1
	d = dict()
	z = 1
	for i in range(sq):
		if z % m == y: return i
		d[y * z % m] = i
		z *= x
		z %= m
	g = pow(x, sq, m)
	z = g
	for i in range(1, sq + 1):
		if z in d:
			num = d[z]
			res = i * sq - num
			return res if pow(x, res, m) == y else -1
		z *= g
		z %= m
	return -1