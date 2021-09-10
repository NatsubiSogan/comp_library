import typing

# 拡張Euclidの互除法
def extgcd(a: int, b: int, d: int = 0) -> typing.Tuple[int, int, int]:
	g = a
	if b == 0:
		x, y = 1, 0
	else:
		x, y, g = extgcd(b, a % b)
		x, y = y, x - a // b * y
	return x, y, g