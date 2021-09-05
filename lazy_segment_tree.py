import typing

# 遅延セグ木

class LazySegmentTree:
	def __init__(
            self, 
            lis: list, 
            op: typing.Callable[[typing.Any, typing.Any], typing.Any], 
            ele: typing.Any, 
            mapp: typing.Callable[[typing.Any, typing.Any], typing.Any], 
            comp: typing.Callable[[typing.Any, typing.Any], typing.Any], 
            id: typing.Any) -> None:
		self.lis = lis
		self.n = len(lis)
		self.op = op
		self.ele = ele
		self.mapp = mapp
		self.comp = comp
		self.id = id
		self.log = (self.n - 1).bit_length()
		self.size = 1 << self.log
		self.data = [ele] * (2 * self.size)
		self.lazy = [id] * self.size
		self._build(lis)

	def update(self, k: int) -> None:
		self.data[k] = self.op(self.data[2 * k], self.data[2 * k + 1])

	def _build(self, lis: list) -> None:
		for i, l in enumerate(lis, self.size):
			self.data[i] = l
		for i in range(1, self.size)[::-1]:
			self.update(i)

	def __setitem__(self, p: int, x: int) -> None:
		p += self.size
		for i in range(1, self.log + 1)[::-1]:
			self.push(p >> i)
		self.data[p] = x
		for i in range(1, self.log + 1):
			self.update(p >> i)

	def __getitem__(self, p: int) -> typing.Any:
		p += self.size
		for i in range(1, self.log + 1):
			self.push(p >> i)
		return self.data[p]

	def apply(self, p: int, f: typing.Optional[typing.Any]) -> None:
		p += self.size
		for i in range(1, self.log + 1)[::-1]:
			self.push(p >> i)
		self.data[p] = self.mapp(f, self.data[p])
		for i in range(1, self.log + 1):
			self.update(p >> i)

	def range_apply(self, l: int, r: int, f: typing.Optional[typing.Any]) -> None:
		if l == r: return 
		l += self.size
		r += self.size
		for i in range(1, self.log + 1)[::-1]:
			if ((l >> i) << i) != l:
				self.push(l >> i)
			if ((r >> i) << i) != r:
				self.push((r - 1) >> i)
		l2, r2 = l, r
		while l2 < r2:
			if l2 & 1:
				self.all_apply(l2, f)
				l2 += 1
			if r2 & 1:
				r2 -= 1
				self.all_apply(r2, f)
			l2 >>= 1
			r2 >>= 1
		for i in range(1, self.log + 1):
			if ((l >> i) << i) != l:
				self.update(l >> i)
			if ((r >> i) << i) != r:
				self.update((r - 1) >> i)

	def all_apply(self, k: int, f: typing.Optional[typing.Any]) -> None:
		self.data[k] = self.mapp(f, self.data[k])
		if k < self.size:
			self.lazy[k] = self.comp(f, self.lazy[k])

	def push(self, k: int) -> None:
		self.all_apply(2 * k, self.lazy[k])
		self.all_apply(2 * k + 1, self.lazy[k])
		self.lazy[k] = self.id

	def prod(self, l: int, r: int) -> typing.Any:
		if l == r: return self.ele
		l += self.size
		r += self.size
		for i in range(1, self.log + 1)[::-1]:
			if ((l >> i) << i) != l:
				self.push(l >> i)
			if ((r >> i) << i) != r:
				self.push(r >> i)
		sml = smr = self.ele
		while l < r:
			if l & 1:
				sml = self.op(sml, self.data[l])
				l += 1
			if r & 1:
				r -= 1
				smr = self.op(self.data[r], smr)
			l >>= 1
			r >>= 1
		return self.op(sml, smr)

	def all_prod(self) -> typing.Any:
		return self.data[1]

	def max_right(self, l: int, g: typing.Callable[[typing.Any], bool]) -> int:
		if l == self.n: return self.n
		l += self.size
		for i in range(1, self.log + 1)[::-1]:
			self.push(l >> i)
		sm = self.ele
		while True:
			while l % 2 == 0:
				l >>= 1
			if not g(self.op(sm, self.data[l])):
				while l < self.size:
					self.push(l)
					l <<= 1
					if g(self.op(sm, self.data[l])):
						sm = self.op(sm, self.data[l])
						l += 1
				return l - self.size
			sm = self.op(sm, self.data[l])
			l += 1
			if (l & -l) == l: return self.n

	def min_left(self, r: int, g: typing.Callable[[typing.Any], bool]) -> int:
		if r == 0: return 0
		r += self.size
		for i in range(1, self.log + 1)[::-1]:
			self.push((r - 1) >> i)
		sm = self.ele
		while True:
			r -= 1
			while r > 1 and r % 2:
				r >>= 1
			if not g(self.op(self.data[r], sm)):
				while r < self.size:
					self.push(r)
					r = 2 * r + 1
					if g(self.op(self.data[r], sm)):
						sm = self.op(self.data[r], sm)
						r -= 1
				return r + 1 - self.size
			sm = self.op(self.data[r], sm)
			if (r & -r) == r: return 0