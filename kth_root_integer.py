# k 乗根の切り捨て/切り上げ
def root_floor(n: int, k: int) -> int:
	l, r = 0, int(pow(n, 1 / k)) + 10000
	while r - l > 1:
		m = (l + r) // 2
		if pow(m, k) > n:
			r = m
		else:
			l = m
	return l

def root_ceil(n: int, k: int) -> int:
	l, r = 0, int(pow(n, 1 / k)) + 10000
	while r - l > 1:
		m = (l + r) // 2
		if pow(m, k) < n:
			l = m
		else:
			r = m
	return r