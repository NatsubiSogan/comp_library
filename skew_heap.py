import typing

# SkewHeap(遅延伝播)
class SHNode:
	def __init__(self, val: int) -> None:
		self.left = None
		self.right = None
		self.val = val
		self.add = 0

	def lazy(self) -> None:
		if self.left != None: self.left.add += self.add
		if self.right != None: self.right.add += self.add
		self.val += self.add
		self.add = 0

class SkewHeap:
	def __init__(self) -> None:
		self.root = None

	def heapmeld(self, h1: SHNode, h2: SHNode) -> SHNode:
		if h1 == None: return h2
		if h2 == None: return h1
		if h1.val + h1.add > h2.val + h2.add:
			h1, h2 = h2, h1
		h1.lazy()
		h1.right = self.heapmeld(h2, h1.right)
		h1.left, h1.right = h1.right, h1.left
		return h1

	def heappop(self) -> int:
		res = self.root
		res.lazy()
		self.root = self.heapmeld(res.left, res.right)
		return res.val

	def heappush(self, x: int) -> None:
		nh = SHNode(x)
		self.root = self.heapmeld(self.root, nh)

	def heaptop(self) -> typing.Union[int, None]:
		if self.root == None: return None
		return self.root.val

	def heapadd(self, val: int) -> None:
		self.root.add += val
