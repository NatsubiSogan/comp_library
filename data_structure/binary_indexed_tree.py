# BIT
class BinaryIndexedTree():
	def __init__(self, n: int) -> None:
		self.n = 1 << (n.bit_length())
		self.BIT = [0] * (self.n + 1)

	def build(self, init_lis: list) -> None:
		for i, v in enumerate(init_lis):
			self.add(i, v)

	def add(self, i: int, x: int) -> None:
		i += 1
		while i <= self.n:
			self.BIT[i] += x
			i += i & -i
	
	def sum(self, l: int, r: int) -> int:
		return self._sum(r) - self._sum(l)

	def _sum(self, i: int) -> int:
		res = 0
		while i > 0:
			res += self.BIT[i]
			i -= i & -i
		return res

	def binary_search(self, x: int) -> int:
		i = self.n
		while True:
			if i & 1:
				if x > self.BIT[i]:
					i += 1
				break
			if x > self.BIT[i]:
				x -= self.BIT[i]
				i += (i & -i) >> 1
			else:
				i -= (i & -i) >> 1
		return i