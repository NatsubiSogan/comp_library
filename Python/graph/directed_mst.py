import typing

from skew_heap import SkewHeap
from union_find import UnionFind

# 最小全域有向木
def directed_minimum_spanning_tree(n: int, m: int, edges: list, root: int) -> typing.Tuple[int, list]:
	froms = [0] * n
	from_cost = [0] * n
	from_heap = [SkewHeap() for i in range(n)]
	UF = UnionFind(n)
	par = [-1] * m
	stem = [-1] * n
	used = [0] * n
	used[root] = 2
	inds = []
	for i, (u, v, c) in enumerate(edges):
		from_heap[v].heappush(c * m + i)
	res = 0
	for v in range(n):
		if used[v] != 0: continue
		proc = []
		chi = []
		cycle = 0
		while used[v] != 2:
			used[v] = 1
			proc.append(v)
			if from_heap[v].root == None: return -1, [-1] * n
			from_cost[v], ind = divmod(from_heap[v].heappop(), m)
			froms[v] = UF.find(edges[ind][0])
			if stem[v] == -1: stem[v] = ind
			if froms[v] == v: continue
			res += from_cost[v]
			inds.append(ind)
			while cycle:
				par[chi.pop()] = ind
				cycle -= 1
			chi.append(ind)
			if used[froms[v]] == 1:
				p = v
				while True:
					if not from_heap[p].root == None:
						from_heap[p].heapadd(-from_cost[p] * m)
					if p != v:
						UF.unite(v, p)
						from_heap[v].root = from_heap[v].heapmeld(from_heap[v].root, from_heap[p].root)
					p = UF.find(froms[p])
					new_v = UF.find(v)
					from_heap[new_v] = from_heap[v]
					v = new_v
					cycle += 1
					if p == v: break
			else:
				v = froms[v]
		for v in proc:
			used[v] = 2
	visited = [0] * m
	tree = [-1] * n
	for i in inds[::-1]:
		if visited[i]: continue
		u, v, c = edges[i]
		tree[v] = u
		x = stem[v]
		while x != i:
			visited[x] = 1
			x = par[x]
	return res, tree
