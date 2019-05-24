#I used factordb.com to factor n into p and q
p = 564819669946735512444543556507
q = 671998030559713968361666935769

n = 379557705825593928168388035830440307401877224401739990998883
e = 65537
c = 29031324384546867512310480993891916222287719490566042302485

#I did not write the functions egcd and modinv, I found them on the internet
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

#I originally wrote 
#flag = m.decode('hex') 
#but that didn't work because of the trailling L. I countered this by stripping L
flag = m.rstrip("L").decode('hex')
print flag

#The flag was tjctf{RSA_2_3asy}
