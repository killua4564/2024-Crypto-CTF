## Information
|  name   | category | solves | score |   solver   |
|:-------:|:--------:|:------:|:-----:|:----------:|
| Nazdone |  Medium  |   35   |  122  | Killua4564 |

## Description
Nazdone is a cryptographic exercise focused on the practical challenges of generating random prime numbers for real-world applications.

## Writeup
* 由題目可知
  * $(p, q, r)$ 皆為 `params` 的 $m$ 組成的 $f(x)$ 多項式的解
    * 假設 $p = c_{0} * m ^ {r_{0}} + c_{1} * m ^ {r_{1}} + ... + c_{a}$
    * 可以看成 $f(x) = c_{0} * x ^ {r_{0}} + c_{1} * x ^ {r_{1}} + ... + c_{a}$
    * 然後 $p = f(m)$
  * $e = m ^ 3 + z - 2$
  * $n = p * q * r$
  * 給 $n$ 和 $c$ 求 `flag` 的 $m$
* 整數不好分解，如果找到 $m$ 做成 $f(x)$ 就會比較好分解，畢竟 $0 \le c_{i} \le 2$
  * 把 $n$ 拿去 `digits(m)` 做成 $m$ 進位來肉眼暴搜 $m$，找到 $m = 19$
```python
m = 19
poly = sum(e * x ** i for i, e in enumerate(Integer(n).digits(m)))
(p, _), (q, _), (r, _) = poly.factor_list()
p, q, r = p(x=m), q(x=m), r(x=m)
assert p * q * r == n
```
* 途中把分解的方程印出來，算一下大概 $z \ge 10$，暴搜一下
```python
for z in itertools.count(10):
    with contextlib.suppress(ZeroDivisionError, UnicodeDecodeError):
        e = m ** 3 + z - 2
        d = inverse_mod(e, (p - 1) * (q - 1) * (r - 1))
        print(long_to_bytes(pow(c, int(d), n)).decode())
        break
```

## Flag
`CCTF{nUmb3r5_1N_D!fFerEn7_8As35_4r3_n!cE!?}`
