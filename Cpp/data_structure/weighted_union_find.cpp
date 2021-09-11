#include <vector>
#include <cassert>

template <typename T>
struct weighted_union_find {
	public:
		weighted_union_find(int size) {
			n = size;
			parent.resize(n);
			rank.resize(n);
			weight.resize(n);
			for (int i = 0; i < n; i++) parent[i] = i;
		}

		int find(int x) {
			assert(0 <= x && x < n);
			if (parent[x] == x) return x;
			else {
				int y = find(parent[x]);
				weight[x] += weight[parent[x]];
				parent[x] = y;
				return y;
			}
		}

		void unite(int x, int y, T w) {
			assert(0 <= x && x < n);
			assert(0 <= y && y < n);
			int p = find(x), q = find(y);
			if (rank[p] < rank[q]) {
				parent[p] = q;
				weight[p] = w - weight[x] + weight[y];
			} else {
				parent[q] = p;
				weight[q] = -w - weight[y] + weight[x];
				if (rank[p] == rank[q]) rank[p]++;
			}
		}

		bool same(int x, int y) {
			assert(0 <= x && x < n);
			assert(0 <= y && y < n);
			return find(x) == find(y);
		}

		T difference(int x, int y) {
			return weight[x] - weight[y];
		}
	private:
		int n;
		std::vector<int> parent, rank;
		std::vector<T> weight;
};