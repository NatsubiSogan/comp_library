# Floor-Sum
def floor_sum(n: int, m: int, a: int, b: int) -> int:
	res = 0
	if a >= m:
		res += (n - 1) * n * (a // m) // 2
		a %= m
	if b >= m:
		res += n * (b // m)
		b %= m
	y_max = (a * n + b) // m
	x_max = y_max * m - b
	if y_max == 0:
		return res
	res += y_max * (n + (-x_max // a))
	res += floor_sum(y_max, a, m, (a - x_max % a) % a)
	return res