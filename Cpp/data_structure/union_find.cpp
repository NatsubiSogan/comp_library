#include <iostream>
#include <cassert>
#include <vector>

struct union_find {
	public:
		union_find(int size) {
			n = size;
			parent.resize(n);
			rank.resize(n);
			for (int i = 0; i < n; i++) {
				parent[i] = i;
				rank[i] = 1;
			}
			cnt = n;
		}

		int find(int x) {
			assert(0 <= x && x < n);
			if (parent[x] == x) return x;
			return parent[x] = find(parent[x]);
		}

		int unite(int x, int y) {
			assert(0 <= x && x < n);
			assert(0 <= y && y < n);
			int p = find(x), q = find(y);
			if (p == q) return p;
			if (p > q) std::swap(p, q);
			rank[p] += rank[q];
			parent[q] = p;
			cnt -= 1;
			return p;
		}
	
	bool same(int x, int y) {
		assert(0 <= x && x < n);
		assert(0 <= y && y < n);
		return find(x) == find(y);
	}

	int size(int x) {
		assert(0 <= x && x < n);
		return rank[x];
	}

	int count() {
		return cnt;
	}

	private:
		int n, cnt;
		std::vector<int> parent, rank;
};

int main() {
	int n, q, t, u, v;
	std::cin >> n >> q;
	union_find uf(n);
	for (int i = 0; i < q ; i++) {
		std::cin >> t >> u >> v;
		if (t == 0) uf.unite(u, v);
		else {
			if (uf.same(u, v)) std::cout << 1 << std::endl;
			else std::cout << 0 << std::endl;
		}
	}
}