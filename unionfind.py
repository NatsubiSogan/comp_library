# Union-Find
class UnionFind():
	def __init__(self, n: int) -> None:
		self.n = n
		self.par = list(range(self.n))
		self.rank = [1] * self.n
		self.count = self.n

	def find(self, x: int) -> int:
		if self.par[x] == x:
			return x
		else:
			self.par[x] = self.find(self.par[x])
			return self.par[x]

	def unite(self, x: int, y: int) -> None:
		p = self.find(x)
		q = self.find(y)
		if p == q:
			return None
		if p > q:
			p, q = q, p
		self.rank[p] += self.rank[q]
		self.par[q] = p
		self.count -= 1

	def same(self, x: int, y: int) -> bool:
		return self.find(x) == self.find(y)

	def size(self, x: int) -> int:
		return self.rank[x]

	def count(self) -> int:
		return self.count