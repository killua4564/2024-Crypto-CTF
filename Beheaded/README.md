## Information
|   name   | category | solves | score | solver  |
|:--------:|:--------:|:------:|:-----:|:-------:|
| Beheaded |   Easy   |   32   |  131  | Curious |

## Description
The beheaded flags have had their headers removed, making them encrypted. Can a living entity truly survive without a head?

## Writeup
分析一下 `behead_me.sh`

```shell
#!/bin/bash

source secrets.sh

FLAGS="all_flags.txt"
rm -f "all_flags.enc"

while read flag; do
	magick -background white -fill blue -pointsize 72 -size "$X"x"$Y" -gravity North caption:"$flag" flag.ppm
	tail -n +4 flag.ppm > tail
	openssl enc -aes-256-ecb -pbkdf2 -nosalt -pass pass:"$KEY" -in tail >> "all_flags.enc"
done < "$FLAGS"
```

基本上他就是把 `all_flags.txt` 一行一行讀到 `$flag` 這個變數中，然後用 

```shell
magick -background white -fill blue -pointsize 72 -size "$X"x"$Y" -gravity North caption:"$flag" flag.ppm
```

這個 command 生成一個白底藍字 `$X` x `$Y` 的 `flag.ppm`，其中的文字內容就是剛剛讀的 `$flag`。接著把 `flag.ppm` 的前三行去掉後用 AES ECB 加密整張圖片，然後再附加到 `all_flags.enc` 後面。

首先先確定 PPM 的檔案格式和 `magick` 會生出什麼。用以下的 command 生一張測試的 PPM

```shell
magick -background white -fill blue -pointsize 72 -size "500"x"100" -gravity North caption:"FLAG{test}" ppm-test.ppm
```

看一下生出來的 `ppm-test.ppm`，配合上 [這個網站](https://netpbm.sourceforge.net/doc/ppm.html)，可以知道用 `magick` 生出來的檔案前三行大約會長

```
P6
<width> <height>
65535
```

接下來的資料猜測是 6 bytes 代表一個 pixel，這一個 pixel 又分成 r, g, b 三組各佔兩個 bytes，這兩個 bytes 猜測是一個 byte 重複寫兩次。

用以下的 script 把 PPM 轉成 PNG

```py
from CTFLib.Utils import *
from CTFLib.Misc import *

with open('ppm-test.ppm', 'rb') as f:
    for _ in range(3):
        f.readline()

    buf = f.read()

pixel_list = [(buf[i], buf[i + 2], buf[i + 4]) for i in range(0, len(buf), 6)]
width, height = 500, 100

PNGConverter.list2png(pixel_list, width, height, 'ppm-test.png')
```

看一下轉換出來的 `ppm-test.png`，看起來我的猜測並沒有問題

![](img/ppm-test.png)

然後再回去看一下 `ppm-test.ppm`，可以發現因為大多數的 pixel 都是白色，所以 `ppm-test.ppm` 的資料大多數都是 `\xff`。

利用這個特點，加上因為是 AES ECB 加密，所以可以知道實際上 `db4e86ff76e9183f97a95d7720dc1d31` 這個 `all_flag.enc` 中的 block 對應的就是 `ffffffffffffffffffffffffffffffff`

至於其餘非 `db4e86ff76e9183f97a95d7720dc1d31` 的 block，可以知道對應的明文不是有混到非白色的 pixel，就是 padding。所以可以先把這些 block 轉成 `00000000000000000000000000000000`

```py
from CTFLib.Utils import *
from CTFLib.Misc import *

with open('all_flags.enc', 'rb') as f:
    cipher = f.read()

white_block_cipher = bytes.fromhex('db4e86ff76e9183f97a95d7720dc1d31')
blocks = [
    b'\xff' * 16 if cipher[i: i + 16] == white_block_cipher else b'\0' * 16
    for i in range(0, len(cipher), 16)
]
plain = b''.join(blocks)
```

接著就是要去識別到底有幾張 `flag.ppm` 被存到 `all_flag.enc` 裡面。

我這邊是假設如果每一張 `flag.ppm` 最前面和最後面都會有一串很長的白色 pixel，然後去算有多少條差不多長的白色 pixel

```py
from CTFLib.Utils import *
from CTFLib.Misc import *

with open('all_flags.enc', 'rb') as f:
    cipher = f.read()

white_block_cipher = bytes.fromhex('db4e86ff76e9183f97a95d7720dc1d31')
blocks = [
    b'\xff' * 16 if cipher[i: i + 16] == white_block_cipher else b'\0' * 16
    for i in range(0, len(cipher), 16)
]
plain = b''.join(blocks)

continuous_white_length = []
count = 0
for num in plain:
    if num != 0xff:
        if count == 0:
            continue
        else:
            continuous_white_length.append(count)
            count = 0

    else:
        count += 1

continuous_white_length.sort(reverse=True)

current = order_of_magnitude(continuous_white_length[0])
for i, length in enumerate(continuous_white_length):
    if order_of_magnitude(length) < current:
        image_num = i // 2
        break

print(len(plain) // 16, image_num)
```

這邊可以知道 `image_num` 是 110，而 `plain` 總共有 6293210 個 block。也就是說每一個 PPM 佔用了 57211 個 block，可能會有 152562、152561 或 152560 個 pixel，把他們都分解一下

```
152562 : 2 * 3 * 47 * 541
152561 : 41 * 61 ** 2
152560 : 2 ** 4 * 5 * 1907
```

如果都嘗試一下就可以發現當 `width, height = 3 * 541, 2 * 47` 的時候轉換出來的圖片是對的

可以看到有一堆 fake flag，找到沒有 `FAKE_FLAG` 的就是 flag 了

![](img/flag-40.png)

## Flag
`CCTF{i_LOv3_7He_3C8_cRypTo__PnNgu1n!!}`
