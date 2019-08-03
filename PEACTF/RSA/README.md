# RSA

## Challenge

"Can you help Bob retrieve the two messages for a flag? (Authenticated Channel)[auth_channel.txt] (Encrypted Channel)[enc_channel.txt]"

## Process

By opening up the text files given in the problem, we can determine that this problem is an RSA encryption problem because we are given n, e, and c values.

I wrote [this](enc_breaker.py) python program in order to decrypt the first half of the of the flag.

```
from factordb.factordb import FactorDB

n = 165481207658568424313022356820498512502867488746572300093793
e = 65537
c = 150635433712900935381157860417761227624682377134647578768653

#The Following function accesses FactorDB for the factors of n
def factor(f):
	f = FactorDB(n)
	f.connect()
	return(f.get_factor_list())
p, q = factor(n)
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
#The first half of the flag is peaCTF{f4ct0r
```

Next I wrote [this](auth_breaker.py) python program in order to decrypt the second half of the of the flag.

```
n = 59883006898206291499785811163190956754007806709157091648869
e = 65537
c = 23731413167627600089782741107678182917228038671345300608183
m = pow(c, e, n)
#I cut 0x and L off of m, in order to convert it into ascii
hex = hex(m)[2:]
hex = hex[:-1]
print hex.strip().decode('hex')

#The second half of the flag is 1ng1sfun}
```

enc channel = peaCTF{f4ct0r
auth channel = 1ng1sfun}

The flag is peaCTF{f4ct0r1ng1sfun}