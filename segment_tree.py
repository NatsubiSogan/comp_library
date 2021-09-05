import typing

# Segment Tree
class SegmentTree:
	def __init__(self, lis: list, ele: typing.Any, op: typing.Callable[[typing.Any, typing.Any], typing.Any]) -> None:
		self.n = len(lis)
		self.log = (self.n - 1).bit_length()
		self.size = 1 << self.log
		self.op = op
		self.ele = ele
		self.tree = self._build(lis)

	def _build(self, lis: list) -> list:
		res_tree = [self.ele] * (2 * self.size)
		for i, a in enumerate(lis):
			res_tree[self.size + i] = a
		for i in range(1, self.size)[::-1]:
			res_tree[i] = self.op(res_tree[2 * i], res_tree[2 * i + 1])
		return res_tree

	def __getitem__(self, i: int) -> None:
		return self.tree[self.size + i]

	def __setitem__(self, p: int, x: int) -> None:
		p += self.size
		self.tree[p] = x
		for i in range(1, self.log + 1):
			self.tree[p >> i] = self.op(self.tree[2 * (p >> i)], self.tree[2 * (p >> i) + 1])

	def prod(self, l: int, r: int) -> int:
		l += self.size
		r += self.size
		L = R = self.ele
		while l < r:
			if l & 1:
				L = self.op(L, self.tree[l])
				l += 1
			if r & 1:
				r -= 1
				R = self.op(self.tree[r], R)
			l >>= 1
			r >>= 1
		return self.op(L, R)

	def all_prod(self) -> int:
		return self.tree[1]

	def max_right(self, l: int, f) -> int:
		if l == self.n:
			return self.n
		l += self.size
		sm = self.ele
		while True:
			while l % 2 == 0:
				l >>= 1
			if not f(self.op(sm, self.tree[l])):
				while l < self.size:
					l *= 2
					if f(self.op(sm, self.tree[l])):
						sm = self.op(sm, self.tree[l])
						l += 1
				return l - self.size
			sm = self.op(sm, self.tree[l])
			l += 1
			if (l & -l) == l:
				return self.n

	def min_left(self, r: int, f) -> int:
		if r == 0:
			return 0
		r += self.size
		sm = self.ele
		while True:
			r -= 1
			while r > 1 and (r % 2):
				r >>= 1
			if not f(self.op(self.tree[r], sm)):
				while r < self.size:
					r = 2 * r + 1
					if f(self.op(self.tree[r], sm)):
						sm = self.op(self.tree[r], sm)
						r -= 1
				return r + 1 - self.size
			sm = self.op(self.d[r], sm)
			if (r & -r) == r:
				return 0