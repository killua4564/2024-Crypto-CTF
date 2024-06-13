## Information
|  name  | category | solves | score |   solver   |
|:------:|:--------:|:------:|:-----:|:----------:|
| Vantuk |  Medium  |   51   |  90   | Killua4564 |

## Description
The Vantuk equation is complex, designed to conceal flag components, yet it appears deceptively simple on the surface.

## Writeup
* 這題描述還蠻簡單的，由題目可知
  * $u(a, x, y) = x + \frac{a * x - y}{x ^ 2 + y ^ 2}$
  * $v(a, x, y) = y - \frac{x + a * y}{x ^ 2 + y ^ 2}$
* 題目把 `flag` 拆成 $(m_{1}, m_{2})$，並有個 `nonce` $a$
* 給定 $(A, U, V)$ 求 $(m_{1}, m_{2})$
  * $A = u(5, a, 4 * a) = a + \frac{5 * a - 4 * a}{a ^ 2 + 16 * a ^ 2} = \frac{17 * a ^ 2 + 1}{17 * a}$
  * $U = u(a, m_{1}, m_{2}) = m_{1} + \frac{a * m_{1} - m_{2}}{m_{1} ^ 2 + m_{2} ^ 2} = \frac{m_{1} * (m_{1} ^ 2 + m_{2} ^ 2 + a) - m_{2}}{m_{1} ^ 2 + m_{2}}$
  * $V = v(a, m_{1}, m_{2}) = m_{2} - \frac{m_{1} + a * m_{2}}{m_{1} ^ 2 + m_{2} ^ 2} = \frac{m_{2} * (m_{1} ^ 2 + m_{2} ^ 2 - a) - m_{1}}{m_{1} ^ 2 + m_{2} ^ 2}$
* 首先 $A$ 蠻明顯是最簡分式了，所以直接拿分母把 $a$ 算回來
  * 若 $A$ 不為最簡分數，則必有因子 $k$ 為分子分母的 `gcd`
  * 以分母來看 $k$ 為 $17$ 或 $a$ 的因式
    * 若 $k$ 包含 $17$，則對分子進行約分 $a ^ 2 + \frac{1}{17}$ 為整數(矛盾 $17$ 不符)
  * 設 $a$ 因式裡有個質數 $p$，則需滿足 $p|17 * p ^ 2 + 1$
    * 對分子進行約分 $17 * p + \frac{1}{p}$ 為整數(矛盾 $k$ 不符)
  * 故 $A = \frac{17 * a ^ 2 + 1}{17 * a}$ 為最簡分式
```python
a = Integer(A.denominator() / 17)
assert A == u(Integer(5), a, 4 * a)
```
* 之後定義一下 $(x, y)$ 變數然後 `solve` 出來即可
```python
x, y = var("x, y")
assume([x > 0, y > 0])
sol = solve([
    U.denominator() * (x * (x ** 2 + y ** 2 + a) - y) == U.numerator() * (x ** 2 + y ** 2),
    V.denominator() * (y * (x ** 2 + y ** 2 - a) - x) == V.numerator() * (x ** 2 + y ** 2),
], x, y)

for x0, y0 in sol:
    # RuntimeError: no explicit roots found
    # TypeError: Unable to coerce x0 to an integer
    with contextlib.suppress(RuntimeError, TypeError):
        x0, y0 = Integer(x0.roots()[0][0]), Integer(y0.roots()[0][0])
        assert U == u(a, x0, y0)
        assert V == v(a, x0, y0)
        print((long_to_bytes(x0) + long_to_bytes(y0)).decode())
```

## Flag
`CCTF{d!D_y0U_5oLv3_7HiS_eQu4T!On_wItH_uSing_c0mPlEx_Num8erS!!?}`
