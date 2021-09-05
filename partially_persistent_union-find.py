import bisect

# 部分永続Union-Find
class PartiallyPersistentUnionFind:
	def __init__(self, n: int) -> None:
		self.par = list(range(n))
		self.size = [1] * n
		self.h = [1] * n
		self.s = [[(0, 1)] for i in range(n)]
		self.t = [10 ** 18] * n

	def find(self, x: int, t: int) -> int:
		while self.t[x] <= t:
			x = self.par[x]
		return x

	def unite(self, x: int, y: int, t: int) -> None:
		p = self.find(x, t)
		q = self.find(y, t)
		if p == q:
			return None
		if self.h[q] < self.h[p]:
			self.par[q] = p
			self.t[q] = t
			self.size[p] += self.size[q]
			self.s[p].append((t, self.size[p]))
		else:
			self.par[p] = q
			self.t[p] = t
			self.size[q] += self.size[p]
			self.s[q].append((t, self.size[q]))
			self.h[q] = max(self.h[q], self.h[p] + 1)

	def getsize(self, x: int, t: int = 10 ** 9) -> int:
		p = self.find(x, t)
		ind = bisect.bisect(self.s[p], (t, 10 ** 18)) - 1
		return self.s[p][ind][1]

	def same(self, x: int, y: int, t: int = 10 ** 9) -> int:
		return self.find(x, t) == self.find(y, t)

	def binary_search(self, x: int, y: int) -> int:
		if not self.same(x, y):
			return -1
		l, r = 0, 10 ** 9
		ans = 10 ** 18
		while l < r:
			m = (l + r) // 2
			if self.same(x, y, m):
				ans = min(ans, m)
				r = m
			else:
				l = m
		return ans + 1