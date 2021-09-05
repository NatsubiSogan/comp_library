import typing

# 中国剰余定理

def invgcd(a: int, b: int) -> typing.Tuple[int, int]:
	a %= b
	if a == 0: return (b, 0)
	s, t, m0, m1 = b, a, 0, 1
	while t:
		u = s // t
		s %= t
		m0 -= m1 * u
		s, t = t, s
		m0, m1 = m1, m0
	if m0 < 0: m0 += b // s
	return (s, m0)

def garner(r: list, m: list) -> typing.Tuple[int, int]:
	n = len(r)
	r0, m0 = 0, 1
	for i in range(n):
		r1, m1 = r[i] % m[i], m[i]
		if m0 < m1:
			r0, r1 = r1, r0
			m0, m1 = m1, m0
		if m0 % m1 == 0:
			if r0 % m1 != r1: return (0, 0)
			continue
		g, im = invgcd(m0, m1)
		u1 = m1 // g
		if (r1 - r0) % g: return (0, 0)
		x = (r1 - r0) // g % u1 * im % u1
		r0 += x * m0
		m0 *= u1
		if r0 < 0: r0 += m0
	return (r0, m0)