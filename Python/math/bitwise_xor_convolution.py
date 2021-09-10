from invmod import invmod

# Bitwise Xor Convolution
class BitwiseXorConvolution:
	def __init__(self, mod: int = 998244353) -> None:
		self.mod = mod

	def fast_hadamard_transform(self, a: list) -> list:
		n = len(a)
		b = (n - 1).bit_length()
		for i in range(b):
			bit = 1 << i
			for j in range(n):
				if not bit & j:
					x, y = a[j], a[j | bit]
					a[j] = (x + y) % self.mod
					a[j | bit] = (x - y) % self.mod
		return a

	def inv_fast_hadamard_transform(self, a: list) -> list:
		a = self.fast_hadamard_transform(a)
		n = len(a)
		inv = invmod(n, self.mod)
		for i in range(n):
			a[i] *= inv
			a[i] %= self.mod
		return a

	def bitwise_xor_convolution(self, a: list, b: list) -> list:
		A = self.fast_hadamard_transform(a)
		B = self.fast_hadamard_transform(b)
		n = len(a)
		C = [i * j for i, j in zip(A, B)]
		C = self.inv_fast_hadamard_transform(C)
		return C