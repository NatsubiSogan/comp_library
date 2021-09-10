# nCrなど
class Combinatorics:
	def __init__(self, n: int, mod: int = 998244353) -> None:
		self.n = n
		self.fa = [1] * (self.n + 1)
		self.fi = [1] * (self.n + 1)
		self.mod = mod

		for i in range(1, self.n + 1):
			self.fa[i] = self.fa[i - 1] * i % self.mod

		self.fi[-1] = pow(self.fa[-1], self.mod - 2, self.mod)

		for i in range(self.n, 0, -1):
			self.fi[i - 1] = self.fi[i] * i % self.mod

	def comb(self, n: int, r: int) -> int:
		if n < r:return 0
		if n < 0 or r < 0:return 0
		return self.fa[n] * self.fi[r] % self.mod * self.fi[n - r] % self.mod

	def perm(self, n: int, r: int) -> int:
		if n < r:return 0
		if n < 0 or r < 0:return 0
		return self.fa[n] * self.fi[n - r] % self.mod
		
	def combr(self, n: int, r: int) -> int:
		if n == r == 0:return 1
		return self.comb(n + r - 1, r)
	