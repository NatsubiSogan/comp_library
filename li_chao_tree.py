import typing

# Li-Chao-Tree
class LiChaoTree:
	def __init__(self, x_list: list, INF: int = 10 ** 18) -> None:
		x_list = sorted(list(set(x_list)))
		self.comp = {x : k for k, x in enumerate(x_list)}
		self.log = (len(x_list) - 1).bit_length()
		self.n = 1 << self.log
		self.ele = (0, INF)
		self.xs = x_list + [INF] * (self.n - len(x_list))
		self.inf = INF
		self.tree = [self.ele for _ in range(2 * self.n)]

	def f(self, line: typing.Tuple[int, int], x: int) -> int:
		a, b = line
		return a * x + b

	def _add_(self, line: typing.Tuple[int, int], ind: int, left: int, right: int) -> None:
		while True:
			mid = (left + right) // 2
			lx = self.xs[left]
			mx = self.xs[mid]
			rx = self.xs[right - 1]
			lu = self.f(line, lx) < self.f(self.tree[ind], lx)
			mu = self.f(line, mx) < self.f(self.tree[ind], mx)
			ru = self.f(line, rx) < self.f(self.tree[ind], rx)
			if lu and ru:
				self.tree[ind] = line
				return
			if not lu and not ru:
				return
			if mu:
				self.tree[ind], line = line, self.tree[ind]
			if lu != mu:
				right = mid
				ind = ind * 2
			else:
				left = mid
				ind = ind * 2 + 1

	def add_line(self, line: typing.Tuple[int, int]) -> None:
		self._add_(line, 1, 0, self.n)

	def add_segment(self, line: typing.Tuple[int, int], left: int, right: int) -> None:
		lind, rind = self.comp[left] + self.n, self.comp[right] + self.n
		left, right = self.comp[left], self.comp[right]
		size = 1
		while lind < rind:
			if lind & 1:
				self._add_(line, lind, left, left + size)
				lind += 1
				left += size
			if rind & 1:
				rind -= 1
				right -= size
				self._add_(line, rind, right, right + size)
			lind >>= 1
			rind >>= 1
			size <<= 1

	def get_min(self, x: int) -> int:
		ind = self.comp[x] + self.n
		res = self.inf
		while ind:
			res = min(res, self.f(self.tree[ind], x))
			ind >>= 1
		return res