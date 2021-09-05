import persistent_array 

# 完全永続Union-Find
class PersistentUnionFind:
	def __init__(self, n: int) -> None:
		self.par = persistent_array.PersistentArray()
		self.rt = self.par.build([-1] * n)
	
	def find(self, x: int, t: int) -> None:
		p = self.par.get(x, t)
		if p < 0: return x
		return self.find(p, t)

	def unite(self, x: int, y: int, t: int) -> int:
		p = self.find(x, t)
		q = self.find(y, t)
		if x == y: return t
		px = self.par.get(p, t)
		qy = self.par.get(q, t)
		if px > qy:
			p, q = q, p
		tmp = self.par.set(q, p, t)
		return self.par.set(p, px + qy, tmp)