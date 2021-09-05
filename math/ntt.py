from invmod import invmod

class NumberTheoreticTransform:
	def primitive_root(self, m: int) -> int:
		if m == 2: return 1
		if m == 167772161: return 3
		if m == 469762049: return 3
		if m == 754974721: return 11
		if m == 998244353: return 3
		divs = [0] * 20
		divs[0] = 2
		cnt = 1
		x = (m - 1) // 2
		while x % 2 == 0: x //= 2
		i = 3
		while i ** 2 <= x:
			if x % i == 0:
				divs[cnt] = i
				cnt += 1
				while x % i == 0: x //= i
		if x > 1:
			divs[cnt] = x
			cnt += 1
		g = 2
		while True:
			f = True
			for i in range(cnt):
				if pow(g, (m - 1) // divs[i], m) == 1: break
			else:
				return g
			g += 1

	def bsf(self, x: int) -> int:
		res = 0
		while x % 2 == 0:
			res += 1
			x //= 2
		return res

	def __init__(self, mod: int = 998244353) -> None:
		self.mod = mod
		self.g = self.primitive_root(self.mod)

	def butterfly(self, a: list) -> None:
		n = len(a)
		h = (n - 1).bit_length()
		sum_e = [0] * 30
		first = True
		if first:
			first = False
			es = [0] * 30
			ies = [0] * 30
			cnt2 = self.bsf(self.mod - 1)
			e = pow(self.g, (self.mod - 1) >> cnt2, self.mod)
			ie = invmod(e, self.mod)
			for i in range(cnt2, 1, -1):
				es[i - 2] = e
				ies[i - 2] = ie
				e = e ** 2 % self.mod
				ie = ie ** 2 % self.mod
			now = 1
			for i in range(cnt2 - 2):
				sum_e[i] = es[i] * now % self.mod
				now = now * ies[i] % self.mod
		for ph in range(1, h + 1):
			w = 1 << (ph - 1)
			p = 1 << (h - ph)
			now = 1
			for s in range(w):
				offset = s << (h - ph + 1)
				for i in range(p):
					l = a[i + offset]
					r = a[i + offset + p] * now % self.mod
					a[i + offset] = (l + r) % self.mod
					a[i + offset + p] = (l - r) % self.mod
				now = now * sum_e[(~s & -~s).bit_length() - 1] % self.mod

	def butterfly_inv(self, a: list) -> None:
		n = len(a)
		h = (n - 1).bit_length()
		sum_ie = [0] * 30
		first = True
		if first:
			first = False
			es = [0] * 30
			ies = [0] * 30
			cnt2 = self.bsf(self.mod - 1)
			e = pow(self.g, (self.mod - 1) >> cnt2, self.mod)
			ie = invmod(e, self.mod)
			for i in range(cnt2, 1, -1):
				es[i - 2] = e
				ies[i - 2] = ie
				e = e ** 2 % self.mod
				ie = ie ** 2 % self.mod
			now = 1
			for i in range(cnt2 - 2):
				sum_ie[i] = ies[i] * now % self.mod
				now = now * es[i] % self.mod
		for ph in range(h, 0, -1):
			w = 1 << (ph - 1)
			p = 1 << (h - ph)
			inow = 1
			for s in range(w):
				offset = s << (h - ph + 1)
				for i in range(p):
					l = a[i + offset]
					r = a[i + offset + p]
					a[i + offset] = (l + r) % self.mod
					a[i + offset + p] = (l - r) * inow % self.mod
				inow = inow * sum_ie[(~s & -~s).bit_length() - 1] % self.mod

	def convolution(self, a: list, b: list) -> list:
		n = len(a)
		m = len(b)
		if not a or not b: return []
		z = 1 << ((n + m - 2).bit_length())
		a += [0] * (z - n)
		b += [0] * (z - m)
		self.butterfly(a)
		self.butterfly(b)
		c = [0] * z
		for i in range(z):
			c[i] = (a[i] * b[i]) % self.mod
		self.butterfly_inv(c)
		iz = invmod(z, self.mod)
		for i in range(n + m - 1):
			c[i] = c[i] * iz % self.mod
		return c[:n + m - 1]