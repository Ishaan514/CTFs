n= 99157116611790833573985267443453374677300242114595736901854871276546481648883
g= 99157116611790833573985267443453374677300242114595736901854871276546481648884
c= 2433283484328067719826123652791700922735828879195114568755579061061723786565164234075183183699826399799223318790711772573290060335232568738641793425546869

p = 310013024566643256138761337388255591613
q = 319848228152346890121384041219876391791

#I did not create the functions gcd, inverse_of, or extended_euclidean_algorithm, I found them on the internet
def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
    

def inverse_of(n, p):
    """
    Returns the multiplicative inverse of
    n modulo p.

    This function returns an integer m such that
    (n * m) % p == 1.
    """
    gcd, x, y = extended_euclidean_algorithm(n, p)
    assert (n * x + p * y) % p == gcd

    if gcd != 1:
        # Either n is 0, or p is not a prime number.
        raise ValueError(
            '{} has no multiplicative inverse '
            'modulo {}'.format(n, p))
    else:
        return x % p

def extended_euclidean_algorithm(a, b):
    """
    Returns a three-tuple (gcd, x, y) such that
    a * x + b * y == gcd, where gcd is the greatest
    common divisor of a and b.

    This function implements the extended Euclidean
    algorithm and runs in O(log b) in the worst case.
    """
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t

#In order to do the decryption math below I followed the wikipedia article on the paillier cryptosystem
def L(x):
	return ((x-1)//n)

	
Lambda = (p-1)*(q-1)//gcd(p-1,q-1)
mu = inverse_of((L(pow(g,Lambda,n**2))),n)
m = L(pow(c,Lambda,n**2))*mu%n
print(hex(m))
#Prints 0x616374667b63727970746f5f6c697665737dL which when placed in a hex to ascii online converter gives the flag
#actf{crypto_lives}