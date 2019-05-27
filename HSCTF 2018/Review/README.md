# Review

## Challenge

'Keith found this cool site and told me to check it out at nc shell.hsctf.com 10000!
Files: review [review.c](review.c)'

## Process
By looking at the source c file, we can determine that this is a buffer overflow problem because the function gets() is used. We want to overwrite the variable valid with any value other than 0 to get the flag. The buffer is set to 32, so as long as we input more than 32 characters our review will become valid. I inputted more than 32 random characters and got the flag.

The flag is: flag{r0tt3n_p0t4t035_rul3z!!!}

