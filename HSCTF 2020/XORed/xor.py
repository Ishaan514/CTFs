'''
 Key 1 = 5dcec311ab1a88ff66b69ef46d4aba1aee814fe00a4342055c146533 
 Key 1 ^ Key 3 = 9a13ea39f27a12000e083a860f1bd26e4a126e68965cc48bee3fa11b 
 Key 2 ^ Key 3 ^ Key 5 = 557ce6335808f3b812ce31c7230ddea9fb32bbaeaf8f0d4a540b4f05 
 Key 1 ^ Key 4 ^ Key 5 = 7b33428eb14e4b54f2f4a3acaeab1c2733e4ab6bebc68436177128eb 
 Key 3 ^ Key 4 = 996e59a867c171397fc8342b5f9a61d90bda51403ff6326303cb865a 
 Flag ^ Key 1 ^ Key 2 ^ Key 3 ^ Key 4 ^ Key 5 = 306d34c5b6dda0f53c7a0f5a2ce4596cfea5ecb676169dd7d5931139
'''
Key_1 = int("5dcec311ab1a88ff66b69ef46d4aba1aee814fe00a4342055c146533", 16)
Key_3 = int("9a13ea39f27a12000e083a860f1bd26e4a126e68965cc48bee3fa11b", 16) ^ Key_1
Key_1234 = int("557ce6335808f3b812ce31c7230ddea9fb32bbaeaf8f0d4a540b4f05",16) ^ int("7b33428eb14e4b54f2f4a3acaeab1c2733e4ab6bebc68436177128eb", 16)
Key_2 = Key_1234^int("996e59a867c171397fc8342b5f9a61d90bda51403ff6326303cb865a",16)^Key_1
flag = int("306d34c5b6dda0f53c7a0f5a2ce4596cfea5ecb676169dd7d5931139",16)^int("7b33428eb14e4b54f2f4a3acaeab1c2733e4ab6bebc68436177128eb",16)^Key_2^Key_3
print(str(hex(flag))[2:-1].decode("hex"))

# The flag is flag{n0t_t00_h4rD_h0p3fully}