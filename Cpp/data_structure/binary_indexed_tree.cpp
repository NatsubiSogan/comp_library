#include <iostream>
#include <vector>
#include <cassert>

template <typename T>
struct binary_indexed_tree {
	public:
		binary_indexed_tree(int size, std::vector<T> init_list) {
			n = 1;
			while (n < size) n *= 2;
			bit_list.resize(n + 1);
			for (int i = 0; i < size; i++) add(i, init_list[i]);
		}

		void add(int i, T x) {
			assert(0 <= i && i < n);
			i++;
			while (i <= n) {
				bit_list[i] += x;
				i += i & -i;
			}
		}

		T sum(int l, int r) {
			assert(0 <= l && l <= r && r <= n);
			return _sum(r) - _sum(l);
		}

		int binary_search(T x) {
			int i = n;
			while (true) {
				if (i & 1) {
					if (x > bit_list[i]) i += 1;
					break;
				}
				if (x > bit_list[i]) {
					x -= bit_list[i];
					i += (i & -i) >> 1;
				} else {
					i -= (i & -i) >> 1;
				}
			}
			return i;
		}
	private:
		int n;
		std::vector<T> bit_list;
		T _sum(int i) {
			T res = 0;
			while (i > 0) {
				res += bit_list[i];
				i -= i & -i;
			}
			return res;
		}
};