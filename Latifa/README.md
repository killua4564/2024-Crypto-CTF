## Information
|  name  | category | solves | score |   solver   |
|:------:|:--------:|:------:|:-----:|:----------:|
| Latifa |   Hard   |   22   |  174  | Killua4564 |

## Description
Latifa is a tricky yet enjoyable challenge, akin to solving a puzzle in a dream-like state.

## Writeup
* 這題我大概用光了整場比賽的運氣，整題靠猜
* 由題目可知
  * $c = \Sigma_{i=0}^{m-1} \frac{b * g}{g ^ {\frac{2 * i}{m}} + g}$
  * $c \gt \Sigma_{i=0}^{m-1} \frac{b * g}{g ^ {\frac{2 * m}{m}} + g}$
  * $c \gt \Sigma_{i=0}^{m-1} \frac{b * g}{g * (g + 1)}$
  * $c \gt \Sigma_{i=0}^{m-1} \frac{b}{g + 1}$
  * $c \gt \frac{m * b}{g + 1}$
* 然後觀察 `output.txt`
  * $c = 1.802740943639362458394687428102524270510281665315 * 10 ^ {47}$
  * $c = 180274094363936245839468742810252427051028166531.5$
    * 所以 $g + 1$ 應該是 $2$ 的倍數
  * $2 * c = 360548188727872491678937485620504854102056333063$
    * 把 $2 * c$ 做 factor 可以得到 $3 * 379 * 39719 * 8959787 * 891059823255825019255461632769683$
    * 然後想到 $c$ 在 txt 裏面小數位有 11955 位，而題目又有一段是 `n(xxx, prec = b)`，那猜猜 $b = 39719$
* 就發現...flag 出現了
```python
print(long_to_bytes(int(c * 2) / 39719).decode())
```

## Flag
`CCTF{h4Lf_7UrN_5ym3Try!}`
