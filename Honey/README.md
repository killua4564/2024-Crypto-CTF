## Information
| name  | category | solves | score |   solver   |
|:-----:|:--------:|:------:|:-----:|:----------:|
| Honey |  Medium  |   48   |  95   | Killua4564 |

## Description
Honey is a concealed cryptographic algorithm designed to provide secure encryption for sensitive messages.

## Writeup
* 由題目可知
  * $nbit = 512$
  * $1 \le Q, R, S \le p - 1$
  * $C = m * Q + r * R + s * S \mod{p}$ (for each)
    * $1 \le r, s \le 2 ^ {\sqrt{nbit / 2}}$
  * 給你 $p$, $Q$, $R$, $S$, $C$ 求 $m$
* 看到這邊很明顯是 `LLL` 了，每兩式把 $m$ 消掉可以把 $(r, s)$ 求出來 (所以其實只需要兩個 $c$)
  * $m * Q_{0} + r_{0} * R_{0} + s_{0} * S_{0} = C_{0}$
  * $m * Q_{1} + r_{1} * R_{1} + s_{1} * S_{1} = C_{1}$
  * $m + r_{0} * R_{0} * Q_{0} ^ {-1} + s_{0} * S_{0} * Q_{0} ^ {-1} = C_{0} * Q_{0} ^ {-1}$
  * $m + r_{1} * R_{1} * Q_{1} ^ {-1} + s_{1} * S_{1} * Q_{1} ^ {-1} = C_{1} * Q_{1} ^ {-1}$
  * $r_{0} * R_{0} * Q_{0} ^ {-1} + s_{0} * S_{0} * Q_{0} ^ {-1} - r_{1} * R_{1} * Q_{1} ^ {-1} - s_{1} * S_{1} * Q_{1} ^ {-1} = C_{0} * Q_{0} ^ {-1} - C_{1} * Q_{1} ^ {-1}$
```python
Matrix([
  [1, 0, 0, 0, 0, int(R[0] * Q[0]^-1)],
  [0, 1, 0, 0, 0, int(S[0] * Q[0]^-1)],
  [0, 0, 1, 0, 0, int(R[1] * Q[1]^-1)],
  [0, 0, 0, 1, 0, int(S[1] * Q[1]^-1)],
  [0, 0, 0, 0, 1, -p],
  [0, 0, 0, 0, 0, int(C[0] * Q[0]^-1 - C[1] * Q[1]^-1)],
]).LLL()
```
* 拿一組順眼的 $(s, r)$ 把 $m$ 解回來
  * $(s_{1}, r_{1}) = (3791125439, 2479984130)$
  * $m = (C_{1} - s_{1} * S_{1} - r_{1} * R_{1}) * Q_{1} ^ {-1}$

## Flag
`CCTF{3X7eNdED_H!dD3n_nNm8eR_pR0Bl3m_iN_CCTF!!}`
