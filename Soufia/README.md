## Information
|  name  | category | solves | score | solver  |
|:------:|:--------:|:------:|:-----:|:-------:|
| Soufia |  Medium  |   36   |  119  | Curious |

## Description
The Soufia equation incorporates an undisclosed random oracle function. Can you analyze the equation and infer the unknown function's value?

## Writeup
這題是要解一個方程式 

```
f(t * x) + t * f(x) = f(f(x + y))
```

其中 `t` 是一個常數，然後他還會給兩個初始條件，其中一個是 `f(0) = f_0`，另一個是 `f(a) = f_a` 其中 `f_0` `a` `f_a` 都不固定。

假設 `x = 0` 的話

```
f(0) + t * f(x) = f(f(x))
```

因為 `f` 的值域是整數，所以可以假設對於任何一個 `c`，一定存在 `b` 讓 `f(b) = c`，所以

```
f(0) + t * c = f(c)
```

由此可以透過一開始給的初始條件來算出 t，接著就是帶入求解了


## Flag
`CCTF{A_funCti0nal_3qu4tiOn_iZ_4_7yPe_oF_EquAtioN_tHaT_inv0lVe5_an_unKnOwn_funCt!on_r4tH3r_thAn_juS7_vArIabl3s!!}`
