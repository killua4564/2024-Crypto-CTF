## Information
| name  | category | solves | score |   solver   |
|:-----:|:--------:|:------:|:-----:|:----------:|
| Melek |  Medium  |   66   |  73   | Killua4564 |

## Description
Melek is a secret sharing scheme that may be relatively straightforward to break - what are your thoughts on the best way to approach it?

## Writeup
* 由題目可知
  * $f$ 的常數項為 $m ^ e$， $1 \le e \le p - 1$
  * $f$ 項數為 $t$， $1 \le t \le nbit - 1$
  * 給 $PT$ 為 $t$ 組隨機數對 $(a, f(a))$， $1 \le a \le p - 1$
* $t$ 次多項式給 $t$ 個點座標，拉格朗日插值法
```python
R.<x> = PolynomialRing(GF(p))
f = R.lagrange_polynomial(PT)
c = f.list()[0]
```
* 之後發現 $gcd(e, p - 1) = 2$，但這個小事
```python
d2 = inverse(e // 2, (p - 1) // 2)
m = int(pow(c, d2, p).sqrt())
print(long_to_bytes(m).decode())
```

## Flag
`CCTF{SSS_iZ_4n_3fF!ciEn7_5ecr3T_ShArIn9_alGorItHm!}`
