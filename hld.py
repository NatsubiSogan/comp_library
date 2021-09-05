import typing

# HLD
class HeavyLightDecomposition:
	def __init__(self, G: list) -> None:
		self.G = G
		self.n = len(G)
		self.par = [-1] * self.n
		self.size = [1] * self.n
		self.head = [0] * self.n
		self.preord = [0] * self.n
		self.k = 0
		for v in range(self.n):
			if self.par[v] == -1:
				self.dfs_sz(v)
				self.dfs_hld(v)
	
	def dfs_sz(self, v: int) -> None:
		G = self.G
		stack, order = [v], [v]
		while stack:
			p = stack.pop()
			for u in G[p]:
				if self.par[p] == u: continue
				self.par[u] = p
				stack.append(u)
				order.append(u)
		while order:
			p = order.pop()
			ch = G[p]
			if len(ch) and ch[0] == self.par[p]:
				ch[0], ch[-1] = ch[-1], ch[0]
			for i, u in enumerate(ch):
				if u == self.par[p]: continue
				self.size[p] += self.size[u]
				if self.size[u] > self.size[ch[0]]:
					ch[i], ch[0] = ch[0], ch[i]
	
	def dfs_hld(self, v: int) -> None:
		G = self.G
		stack = [v]
		while stack:
			p = stack.pop()
			self.preord[p] = self.k
			self.k += 1
			top = self.G[p][0]
			for u in G[p][::-1]:
				if u == self.par[p]: continue
				if u == top:
					self.head[u] = self.head[p]
				else:
					self.head[u] = u
				stack.append(u)

	def enumerate_vertices(self, u: int, v: int) -> typing.Union[typing.Tuple[int, int], None]:
		while True:
			if self.preord[u] > self.preord[v]: u, v = v, u
			l = max(self.preord[self.head[v]], self.preord[u])
			r = self.preord[v]
			yield l, r
			if self.head[u] != self.head[v]:
				v = self.par[self.head[v]]
			else:
				return
	
	def enumerate_edges(self, u: int, v: int) -> typing.Tuple[int, int]:
		while True:
			if self.preord[u] > self.preord[v]: u, v = v, u
			if self.head[u] != self.head[v]:
				yield self.preord[self.head[v]], self.preord[v]
				v = self.par[self.head[v]]
			else:
				if u != v:
					yield self.preord[u] + 1, self.preord[v]
				break

	def subtree(self, v: int) -> typing.Tuple[int, int]:
		l = self.preord[v]
		r = self.preord[v] + self.size(v)
		return l, r

	def lowest_common_ancestor(self, u: int, v: int) -> int:
		while True:
			if self.preord[u] > self.preord[v]: u, v = v, u
			if self.head[u] == self.head[v]: return u
			v = self.par[self.head[v]]