from pwn import remote

conn = remote("01.cr.yp.toc.tf", "17113")

for _ in range(20):
    conn.recvuntil(b"f(1, 1) = ")
    t0 = int(conn.recvuntil(b" ").decode())
    conn.recvuntil(b"f(x, y) = ")
    t1 = int(conn.recvuntil(b"\n").decode())
    conn.sendlineafter(b": ", f"{t1 - t0 + 1},{t1 - t0}".encode())
    conn.recvline()
    print(conn.recvline())

conn.interactive()
