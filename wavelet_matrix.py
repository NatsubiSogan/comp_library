from bit_vector import BitVector

# Wavelet Matrix

class WaveletMatrix:
	def __init__(self, array: list, log: int = 32) -> None:
		self.n = len(array)
		self.mat = []
		self.zs = []
		self.log = log
		for d in range(self.log)[::-1]:
			ls, rs = [], []
			BV = BitVector(self.n + 1)
			for ind, val in enumerate(array):
				if val & (1 << d):
					rs.append(val)
					BV.set(ind)
				else:
					ls.append(val)
			BV.build()
			self.mat.append(BV)
			self.zs.append(len(ls))
			array = ls + rs
	
	def access(self, i: int) -> int:
		res = 0
		for d in range(self.log):
			res <<= 1
			if self.mat[d][i]:
				res |= 1
				i = self.mat[d].rank1(i) + self.zs[d]
			else:
				i = self.mat[d].rank0(i)
		return res

	def rank(self, val: int, l: int, r: int) -> int:
		for d in range(self.log):
			if val >> (self.log - d - 1) & 1:
				l = self.mat[d].rank1(l) + self.zs[d]
				r = self.mat[d].rank1(r) + self.zs[d]
			else:
				l = self.mat[d].rank0(l)
				r = self.mat[d].rank0(r)
		return r - l
	
	def quantile(self, l: int, r: int, k: int) -> int:
		res = 0
		for d in range(self.log):
			res <<= 1
			cntl, cntr = self.mat[d].rank1(l), self.mat[d].rank1(r)
			if cntr - cntl >= k:
				l = cntl + self.zs[d]
				r = cntr + self.zs[d]
				res |= 1
			else:
				l -= cntl
				r -= cntr
				k -= cntr - cntl
		return res

	def kth_smallest(self, l: int, r: int, k: int) -> int:
		return self.quantile(l, r, r - l - k)

class CompressedWaveletMatrix:
	def __init__(self, array: list) -> None:
		self.array = sorted(set(array))
		self.comp = {val: ind for ind, val in enumerate(self.array)}
		array = [self.comp[val] for val in array]
		log = len(self.array).bit_length()
		self.WM = WaveletMatrix(array, log)

	def access(self, i: int) -> int:
		return self.array[self.WM.access(i)]

	def rank(self, l: int, r: int, val: int) -> int:
		if val not in self.comp: return 0
		return self.WM.rank(self.comp[val], l, r)
	
	def kth_smallest(self, l: int, r: int, k: int) -> int:
		return self.array[self.WM.kth_smallest(l, r, k)]