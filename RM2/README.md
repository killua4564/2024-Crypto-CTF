## Information
| name | category | solves | score | solver  |
|:----:|:--------:|:------:|:-----:|:-------:|
| RM2  |  Medium  |   64   |  75   | Curious |

## Description
The RM2 cryptosystem is a minimalist design that exhibits remarkable resilience, making it exceptionally difficult to compromise.

## Writeup
這題就是需要找兩個質數 `p` 和 `q`，然後 server 會用 `(e, (p - 1) * (q - 1))` 和 `(e, (2 * p + 1) * (2 * q + 1))` 這兩把公鑰來加密兩段 secret。其實主要這題就是找兩個 `p, q` 減一之後是平滑的且 `2 * p + 1, 2 * q + 1` 都是質數。

## Flag
`CCTF{i_l0v3_5UpeR_S4fE_Pr1m3s!!}`
