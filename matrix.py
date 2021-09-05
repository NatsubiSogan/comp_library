from invmod import invmod

import typing

# 行列ライブラリ(遅い)

class Matrix:
	def __init__(self, n: int, m: int, mat: typing.Union[list, None] = None, mod: int = 998244353) -> None:
		self.n = n
		self.m = m
		self.mat = [[0] * self.m for i in range(self.n)]
		self.mod = mod
		if mat:
			for i in range(self.n):
				self.mat[i] = mat[i]
	
	def is_square(self) -> None:
		return self.n == self.m
	
	def __getitem__(self, key: int) -> int:
		if isinstance(key, slice):
			return self.mat[key]
		else:
			assert key >= 0
			return self.mat[key]

	def id(n: int):
		res = Matrix(n, n)
		for i in range(n):
			res[i][i] = 1
		return res

	def __len__(self) -> int:
		return len(self.mat)
	
	def __str__(self) -> str:
		return "\n".join(" ".join(map(str, self[i])) for i in range(self.n))

	def times(self, k: int):
		res = [[0] * self.m for i in range(self.n)]
		for i in range(self.n):
			for j in range(self.m):
				res[i][j] = k * self[i][j] % self.mod
		return Matrix(self.n, self.m, res)

	def __pos__(self):
		return self

	def __neg__(self):
		return self.times(-1)

	def __add__(self, other):
		res = [[0] * self.m for i in range(self.n)]
		for i in range(self.n):
			for j in range(self.m):
				res[i][j] = (self[i][j] + other[i][j]) % self.mod
		return Matrix(self.n, self.m, res)
	
	def __sub__(self, other):
		res = [[0] * self.m for i in range(self.n)]
		for i in range(self.n):
			for j in range(self.m):
				res[i][j] = (self[i][j] - other[i][j]) % self.mod
		return Matrix(self.n, self.m, res)

	def __mul__(self, other):
		if other.__class__ == Matrix:
			res = [[0] * other.m for i in range(self.n)]
			for i in range(self.n):
				for k in range(self.m):
					for j in range(other.m):
						res[i][j] += self[i][k] * other[k][j]
						res[i][j] %= self.mod
			return Matrix(self.n, other.m, res)
		else:
			return self.times(other)
	
	def __rmul__(self, other):
		return self.times(other)

	def __pow__(self, k):
		tmp = Matrix(self.n, self.n, self.mat)
		res = Matrix.id(self.n)
		while k:
			if k & 1:
				res *= tmp
			tmp *= tmp
			k >>= 1
		return res

	def determinant(self):
		res = 1
		tmp  = Matrix(self.n, self.n, self.mat)
		for j in range(self.n):
			if tmp[j][j] == 0:
				for i in range(j + 1, self.n):
					if tmp[i][j] != 0: break
				else:
					return 0
				tmp.mat[j], tmp.mat[i] = tmp.mat[i], tmp.mat[j]
				res *= -1
			inv = invmod(tmp[j][j], self.mod)
			for i in range(j + 1, self.n):
				c = -inv * tmp[i][j] % self.mod
				for k in range(self.n):
					tmp[i][k] += c * tmp[j][k]
					tmp[i][k] %= self.mod
		for i in range(self.n):
			res *= tmp[i][i]
			res %= self.mod
		return res