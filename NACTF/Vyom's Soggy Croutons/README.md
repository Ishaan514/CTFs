# Vyom's Soggy Croutons

## Challenge

"Vyom was eating a CAESAR salad with a bunch of wet croutons when he sent me this

ertkw{vk_kl_silkv}

Can you help me decipher his message?"

# Process

The challenge description implies that this is a Caesar cipher challenge. I used https://www.dcode.fr/caesar-cipher to brute force the rotation of the Caesar cipher with the input ertkw{vk_kl_silkv}. 

I got NACTFETTUBRUTE, which I then reconstructed into the flag.

The flag is nactf{et_tu_brute}