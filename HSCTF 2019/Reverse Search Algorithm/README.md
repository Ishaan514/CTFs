# Reverse Search Algorithm

## Challenge

"WWPHSN students, gotta get these points to boost your grade.

n = 561985565696052620466091856149686893774419565625295691069663316673425409620917583731032457879432617979438142137

e = 65537

c = 328055279212128616898203809983039708787490384650725890748576927208883055381430000756624369636820903704775835777"

## Process

We can determine that this problem is a typical RSA encryption problem because we are given n, e, and c values.

I wrote [this](RSA_Breaker.py) python program in order to decrypt the flag. I used the website factordb.com to factor n into p and q. 
```
n = 561985565696052620466091856149686893774419565625295691069663316673425409620917583731032457879432617979438142137
e = 65537
c = 328055279212128616898203809983039708787490384650725890748576927208883055381430000756624369636820903704775835777
p = 19378812610208711050554891591368513578428260883630885898953907471497427917962675301070084754463193723428901453
q = 29
#I did not write the egcd and modinv functions, I found them on the internet
def egcd(a, b):
    if a ==0:
        return (b,0,1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

#In order to do the decryption math below I followed the wikipedia article on RSA encryption
phi = (p-1)*(q-1)
d = modinv(e, phi)
m = hex(pow(c,d,n))[2:]
#I cut the last character off m, which is L, in order to decode it into ascii
m = m[:-1]
flag = m.strip().decode('hex')
print flag
#The flag is: hsctf{y3s_rsa_1s_s0lved_10823704961253}
```

The flag is: hsctf{y3s_rsa_1s_s0lved_10823704961253}