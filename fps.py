from invmod import invmod
from ntt import NumberTheoreticTransform

# 形式的冪級数（未完成）
class FormalPowerSeries:
	def __init__(self, n: int, l: list = [], mod: int = 998244353) -> None:
		self.n = n
		self.l = l + [0] * (n - len(l))
		self.mod = mod
	
	def __add__(self, other):
		res = FormalPowerSeries(self.n, [], self.mod)
		for i in range(self.n):
			res.l[i] = self.l[i] + other.l[i]
			res.l[i] %= self.mod
		return res
	
	def __sub__(self, other):
		res = FormalPowerSeries(self.n, [], self.mod)
		for i in range(self.n):
			res.l[i] = self.l[i] - other.l[i]
			res.l[i] %= self.mod
		return res

	def __mul__(self, other):
		res = FormalPowerSeries(self.n, [], self.mod)
		NTT = NumberTheoreticTransform(self.mod)
		cv = NTT.convolution(self.l, other.l)
		for i in range(self.n):
			res.l[i] = cv[i]
		return res
	
	def resize(self, n: int):
		res = FormalPowerSeries(n, [], self.mod)
		for i in range(min(n, self.n)):
			res.l[i] = self.l[i]
		return res

	def times(self, k: int):
		res = FormalPowerSeries(self.n, [], self.mod)
		for i in range(self.n):
			res.l[i] = self.l[i] * k % self.mod
		return res

	def inverse(self):
		r = invmod(self.l[0], self.mod)
		m = 1
		res = FormalPowerSeries(m, [r], self.mod)
		while m < self.n:
			m *= 2
			res = res.resize(m)
			res = res.times(2).subtract(res.multiply(res.resize(m)).multiply(self.resize(m)))
		res = res.resize(self.n)
		return res

	def divide(self, other) -> None:
		self.multiply(self, other.inverse())

	def differentiate(self):
		res = FormalPowerSeries(self.n, [], self.mod)
		for i in range(1, self.n):
			res.l[i - 1] = self.l[i] * i % self.mod
		return res

	def integrate(self):
		res = FormalPowerSeries(self.n, [], self.mod)
		for i in range(self.n - 1):
			res.l[i + 1] = self.l[i] * invmod(i + 1, self.mod)
		return res