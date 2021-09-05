# Bit Vector

class BitVector:
	def __init__(self, size: int) -> None:
		self.block = (size + 31) >> 5
		self.bit = [0] * self.block
		self.cnt = [0] * self.block
	
	def set(self, i: int) -> None:
		self.bit[i >> 5] |= 1 << (i & 31)

	def build(self) -> None:
		for i in range(self.block - 1):
			self.cnt[i + 1] = self.cnt[i] + self.popcount(self.bit[i])

	def popcount(self, x: int) -> int:
		x = x - ((x >> 1) & 0x55555555)
		x = (x & 0x33333333) + ((x >> 2) & 0x33333333)
		x = (x + (x >> 4)) & 0x0f0f0f0f
		x = x + (x >> 8)
		x = x + (x >> 16)
		return x & 0x0000007f
	
	def rank1(self, r: int) -> int:
		msk = (1 << (r & 31)) - 1
		return self.cnt[r >> 5] + self.popcount(self.bit[r >> 5] & msk)

	def rank0(self, r: int) -> int:
		return r - self.rank1(r)