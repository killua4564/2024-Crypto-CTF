from Crypto.Util.number import inverse, long_to_bytes
from sage.all import PolynomialRing, GF

from output_txt import e, p, pt

R = PolynomialRing(GF(p), names=("x",))
f = R.lagrange_polynomial(pt)

c = f.list()[0]
d2 = inverse(e // 2, (p - 1) // 2)
m = int(pow(c, d2, p).sqrt())
print(long_to_bytes(m).decode())
