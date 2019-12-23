# Get a GREP #1!

## Challenge

"Juliet hid a flag among 100,000 dummy ones so I don't know which one is real! But maybe the format of her flag is predictable I know sometimes people add random characters to the end of flags... I think she put 7 random vowels at the end of hers. Can you get a GREP on this flag"

You can download the problem files here [flag.txt](flag.txt)

## Process

I used regular expressions with the grep command to search for a flag in the list of flags which started with nactf{ had 42 unknown charcters and ended in 7 random capital or lowercase vowels. 

```
$ grep 'nactf{..........................................[aeiouAEIOU][aeiouAEIOU][aeiouAEIOU][aeiouAEIOU][aeiouAEIOU][aeiouAEIOU][aeiouAEIOU]}' flag.txt
```

The flag is nactf{r3gul4r_3xpr3ss10ns_ar3_m0r3_th4n_r3gul4r_euaiooa}