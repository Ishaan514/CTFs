# Worth

## Challenge

"This problem is worth 0o511 points.

Hint: Put your answer in the flag format: flag {peactf_}"

## Process

The "0o" prefix at the begginning of "0o511" gave away that the number is octal. It is like the 0x prefix that comes before hexadecimal numbers. I converted the octal number in python to decimal and wrapped it in the flag format. 

```
>>> int('0o511' , 8)
329
```

The flag is flag{peactf_329}

