from extgcd import extgcd

# mod p における逆元
def invmod(a: int, p: int) -> int:
	x, y, g = extgcd(a, p)
	x %= p
	return x