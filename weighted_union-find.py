# 重み付きUnion-Find
class WeightedUnionFind:
	def __init__(self, n):
		self.n = n
		self.par = list(range(n))
		self.rank = [0] * n
		self.weight = [0] * n

	def find(self, x):
		if self.par[x] == x:
			return x
		else:
			y = self.find(self.par[x])
			self.weight[x] += self.weight[self.par[x]]
			self.par[x] = y
			return y

	def unite(self, x, y, w):
		p, q = self.find(x), self.find(y)
		if self.rank[p] < self.rank[q]:
			self.par[p] = q
			self.weight[p] = w - self.weight[x] + self.weight[y]
		else:
			self.par[q] = p
			self.weight[q] = -w - self.weight[y] + self.weight[x]
			if self.rank[p] == self.rank[q]:
				self.rank[p] += 1

	def same(self, x, y):
		return self.find(x) == self.find(y)

	def diff(self, x, y):
		return self.weight[x] - self.weight[y]