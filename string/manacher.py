# Manacher's Algorithm
class Manacher():
	def __init__(self, s: str) -> None:
		self.s = s
	def coustruct(self) -> list:
		i, j = 0, 0
		res = [0] * len(self.s)
		while i < len(self.s):
			while i - j >= 0 and i + j < len(self.s) and self.s[i - j] == self.s[i + j]:
				j += 1
			res[i] = j
			k = 1
			while i - k >= 0 and i + k < len(self.s) and k + res[i - k] < j:
				res[i + k] = res[i - k]
				k += 1
			i += k
			j -= k
		return res