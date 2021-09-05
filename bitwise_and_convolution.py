# Bitwise And Convolution
class BitwiseAndConvolution:
	def __init__(self, mod: int = 998244353) -> None:
		self.mod = mod

	def fast_zeta_transform_and(self, a: list) -> list:
		n = len(a)
		b = (n - 1).bit_length()
		for i in range(b):
			bit = 1 << i
			for j in range(n):
				if not bit & j:
					a[j] += a[bit | j]
					a[j] %= self.mod
		return a

	def fast_mobius_transform_and(self, a: list) -> list:
		n = len(a)
		b = (n - 1).bit_length()
		for i in range(b):
			bit = 1 << i
			for j in range(n):
				if not bit & j:
					a[j] -= a[bit | j]
					a[j] %= self.mod
		return a

	def bitwise_and_convolution(self, a: list, b: list) -> list:
		n = len(a)
		A = self.fast_zeta_transform_and(a)
		B = self.fast_zeta_transform_and(b)
		C = [i * j % self.mod for i, j in zip(A, B)]
		return self.fast_mobius_transform_and(C)