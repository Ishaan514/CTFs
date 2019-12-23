## Get a GREP #0!

## Challenge

"Vikram was climbing a chunky tree when he decided to hide a flag on one of the leaves. There are 10,000 leaves so there's no way you can find the right one in time... Can you open up a terminal window and get a grep on the flag"

You can download the problem files here [bigtree.zip](bigtree.zip)

## Process

The given zip file has a very large amount of files in it. I used the commands strings and grep to quickly find the flag.

```
$ strings bigtree.zip | grep nactf{
```

The flag is nactf{v1kram_and_h1s_10000_l3av3s}