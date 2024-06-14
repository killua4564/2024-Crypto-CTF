from pwn import *

from CTFLib.Utils import *
from CTFLib.Tools import *

payloads = []
for i in range(8):
    payloads.append(fastcoll(bytes([i])))

r = nc('nc 00.cr.yp.toc.tf 13771')

for i in trange(8):
    r.sendlineafter(b':  \n', payloads[i][0].hex().encode())
    r.sendlineafter(b': \n', payloads[i][1].hex().encode())

r.interactive()

