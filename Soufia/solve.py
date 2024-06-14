from pwn import *

from CTFLib.Utils import *

r = nc('nc 00.cr.yp.toc.tf 13377')
r.recvlines(4)

f_0 = int(r.recvline().strip().split()[4][:-1])

result = r.recvline().strip().split()
a = int(result[2][2:-1])
f_a = int(result[4])

t = (f_a - f_0) // a

for i in trange(20):
    r.recvline()
    x = int(r.recvline().strip().split()[4][2:-2])
    r.sendline(str(f_0 + t * x).encode())

r.interactive()