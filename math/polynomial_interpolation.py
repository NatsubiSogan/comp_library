from invmod import invmod

# 多項式補間
class PolynomialInterpolation:
	def __init__(self, mod: int = 99824353) -> None:
		self.mod = mod

	# 多項式補間(普通の O(N^2))
	def polynomial_interpolation(self, X: list, Y: list, t: int) -> int:
		n = len(X) - 1
		c = [0] * (n + 1)
		for i, xi in enumerate(X):
			f = 1
			for j, xj in enumerate(X):
				if i == j: continue
				f *= (xi - xj)
				f %= self.mod
			c[i] = (Y[i] * invmod(f, self.mod)) % self.mod
		res = 0
		f = 1
		for i, x in enumerate(X):
			f *= (t - x)
			f %= self.mod
		for i, a in enumerate(c):
			res += a * f * invmod(t - X[i], self.mod) % self.mod
			res %= self.mod
		return res

	# 多項式補間(等差の O(N log N))
	def polynomial_interpolation_arithmetic(self, a: int, d: int, Y: list, t: int) -> int:
		n = len(Y) - 1
		C = [0] * (n + 1)
		f = 1
		for i in range(1, n + 1):
			f *= -d * i
			f %= self.mod
		C[0] = (Y[0] * invmod(f, self.mod)) % self.mod
		for i in range(1, n + 1):
			f *= invmod(-d * (n - i + 1), self.mod) * d * i
			f %= self.mod
			C[i] = (Y[i] * invmod(f, self.mod)) % self.mod
		res = 0
		f = 1
		for i in range(n + 1):
			f = f * (t - (a + d * i))
			f %= self.mod
		for i, c in enumerate(C):
			res += c * f * invmod(t - (a + d * i), self.mod)
			res %= self.mod
		return res