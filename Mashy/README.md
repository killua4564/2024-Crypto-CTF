## Information
| name  | category | solves | score | solver  |
|:-----:|:--------:|:------:|:-----:|:-------:|
| Mashy |   Easy   |   68   |  71   | Curious |

## Description
Mashy may seem like a simple cracking task, but you'll need to open your eyes to identify the right things to crack.

## Writeup
這題就是需要 input 7 組兩個不同的 hex string，然後這兩個 hex string 和一個不知道是啥的 `salt` md5 之後，xor 起來的 hex 要是 `a483b30944cbf762d4a3afc154aad825`。這邊直接猜測可能需要兩個 hex string 的 md5 一樣，這樣 xor 起來就會一直都是 `salt` 的 md5

## Flag
`CCTF{mD5_h4Sh_cOlL!Si0N_CrYp7o_ch41lEnGe!!!}`
