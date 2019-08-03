# Breakfast

## Challenge

"Mmm I ate some nice **bacon** and eggs this morning. Find out what else I had for an easy flag. Don’t forget to capitalize CTF! [Ciphertext](enc.txt)"

## Process

Emphasis on the word bacon implies that this problem is a bacon cipher problem. The ciphertext also looks like it could have gone through a bacon cipher.

```
011100010000000000101001000101{00100001100011010100000000010100101010100010010001}
```

I decrypted the ciphertext with this website https://www.dcode.fr/bacon-cipher. I then changed the capitalization and added the brackets a second time to get the flag.

The flag is peaCTF{eggwaffles}.