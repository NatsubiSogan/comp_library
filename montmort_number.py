# モンモール数（長さ N の完全順列の数）を 1,2,...,N について求める
def montmort_number(n: int, mod: int = 998244353) -> list:
	res = [0]
	for i in range(2, n + 1): res.append((i * res[-1] + pow(-1, i)) % mod)
	return res