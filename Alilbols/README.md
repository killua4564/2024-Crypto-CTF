## Information
|   name   | category | solves | score |   solver   |
|:--------:|:--------:|:------:|:-----:|:----------:|
| Alilbols |  Medium  |   59   |  80   | Killua4564 |

## Description
Alilbols, a modified version of the Alibos cryptographic algorithm, offers enhanced security features to protect sensitive and confidential data.

## Writeup
* 由題目可知
  * $q = 4 * 100 ^ d$
  * $h = f ^ {-1} * g \mod{q}$
  * $c = r * h + m + r$ (其中 $r$ 為 nonce)
  * 給你 $h$ 和 $c$ 要求出 $m$
* 先猜出 $d$，因為 $h$ 和 $q$ 的量級是差不多的，所以這邊 $d$ 先猜 $563$
```python
d = len(h.digits()) // 2
```
* 然後用 Gauss reduction 求出 SVP $(f, g)$ (這邊沒用 sage)
  * $1 \le f \le \sqrt{2} * 10 ^ d$
  * $10 ^ d \le g \le \sqrt{2} * 10 ^ d$
  * $f * (1, h) - k * (0, q) = (f, g)$
```python
Matrix[[1, h], [0, q]].LLL()
```
* 最後對 `c` 動手腳解出 `m`
  * $c = r * h + m + r \mod{q}$
  * $c * f = r * (f + g) + m * f \mod{q}$
  * $c * f * f ^ {-1} = m \mod{f + g}$

## Flag
`CCTF{4_c0N9rU3n7!aL_Pu81iC_k3Y_cRyp70_5ySTeM_1N_CCTF!!}`
