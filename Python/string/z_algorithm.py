# Z-Algorithm
def z_algorithm(s: str) -> list:
	str_len = len(s)
	res = [0] * str_len
	res[0] = str_len
	i, j = 1, 0
	while i < str_len:
		while i + j < str_len and s[i + j] == s[j]:
			j += 1
		res[i] = j
		if j == 0:
			i += 1
			continue
		k = 1
		while i + k < str_len and j > res[k] + k:
			res[i + k] = res[k]
			k += 1
		i += k
		j -= k
	return res