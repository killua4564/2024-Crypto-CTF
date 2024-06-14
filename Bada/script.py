
from pwn import *
r=remote('01.cr.yp.toc.tf', 17113)

r.recvlines(6)
for i in range(100):
    a=r.recvline().split()
    print(a)
    n1=int(a[6].decode())
    n2=int(a[11].decode())

    m=n2-n1
    print(m)
    r.sendlineafter(b'Please send x, y separated by comma: ',f'{m+1},{m}'.encode())
    r.recvlines(2)
r.interactive()