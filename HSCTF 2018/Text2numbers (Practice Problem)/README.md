# Text2numbers (Practice Problem)

## Challenge

'In order to make text more easily encrypted, it is essential to transform it into some sort of numeric state. A simple way to do this is by taking letters, transforming them into numbers by their place in the alphabet ( a - 1, b - 2, c - 3, and so on), “ ” going to 27, and “_” going to 28. For instance, the string “bad ” would go to the numbers (2,1,4,27). A program to automate this will make things vastly easier for you.
Can you decrypt the flag?

(23, 5, 12, 12, 27, 20, 8, 5, 27, 6, 12, 1, 7, 27, 9, 19, 27, 8, 9, 4, 4, 5, 14, 27, 8, 5, 18, 5, 27, 2, 21, 20, 27, 6, 9, 18, 19, 20, 27, 23, 5, 27, 8, 1, 22, 5, 27, 19, 15, 13, 5, 27, 20, 5, 24, 20, 27, 20, 15, 27, 3, 15, 14, 6, 21, 19, 5, 27, 25, 15, 21, 27, 14, 15, 23, 27, 20, 8, 5, 27, 6, 12, 1, 7, 27, 9, 19, 27, 9, 14, 27, 6, 1, 3, 20, 27, 19, 5, 3, 18, 5, 20, 19, 28, 1, 18, 5, 28, 8, 9, 4, 4, 5, 14, 28, 9, 14, 28, 20, 8, 9, 19, 28, 12, 9, 19, 20, 27, 4, 15, 14, 20, 27, 9, 14, 3, 12, 21, 4, 5, 27, 20, 8, 5, 27, 16, 1, 18, 20, 19, 27, 20, 8, 1, 20, 27, 1, 18, 5, 27, 19, 5, 16, 5, 18, 1, 20, 5, 4, 27, 23, 9, 20, 8, 27, 19, 16, 1, 3, 5, 19)'

## Process

We are told exactly what to do for this problem. Just replace every number with its corresponding letter.

I wrote [this](decoder.py) python program in order to do exactly what is asked.

```
chars = [23, 5, 12, 12, 27, 20, 8, 5, 27, 6, 12, 1, 7, 27, 9, 19, 27, 8, 9, 4, 4, 5, 14, 27, 8, 5, 18, 5, 27, 2, 21, 20, 27, 6, 9, 18, 19, 20, 27, 23, 5, 27, 8, 1, 22, 5, 27, 19, 15, 13, 5, 27, 20, 5, 24, 20, 27, 20, 15, 27, 3, 15, 14, 6, 21, 19, 5, 27, 25, 15, 21, 27, 14, 15, 23, 27, 20, 8, 5, 27, 6, 12, 1, 7, 27, 9, 19, 27, 9, 14, 27, 6, 1, 3, 20, 27, 19, 5, 3, 18, 5, 20, 19, 28, 1, 18, 5, 28, 8, 9, 4, 4, 5, 14, 28, 9, 14, 28, 20, 8, 9, 19, 28, 12, 9, 19, 20, 27, 4, 15, 14, 20, 27, 9, 14, 3, 12, 21, 4, 5, 27, 20, 8, 5, 27, 16, 1, 18, 20, 19, 27, 20, 8, 1, 20, 27, 1, 18, 5, 27, 19, 5, 16, 5, 18, 1, 20, 5, 4, 27, 23, 9, 20, 8, 27, 19, 16, 1, 3, 5, 19]

exp = []
for x in chars:
    if x == 1:
        exp.append("a")
    if x == 2:
        exp.append("b")
    if x == 3:
        exp.append("c")
    if x == 4:
        exp.append("d")
    if x == 5:
        exp.append("e")
    if x == 6:
        exp.append("f")
    if x == 7:
        exp.append("g")
    if x == 8:
        exp.append("h")
    if x == 9:
        exp.append("i")
    if x == 10:
        exp.append("j")
    if x == 11:
        exp.append("k")
    if x == 12:
        exp.append("l")
    if x == 13:
        exp.append("m")
    if x == 14:
        exp.append("n")
    if x == 15:
        exp.append("o")
    if x == 16:
        exp.append("p")
    if x == 17:
        exp.append("q")
    if x == 18:
        exp.append("r")
    if x == 19:
        exp.append("s")
    if x == 20:
        exp.append("t")
    if x == 21:
        exp.append("u")
    if x == 22:
        exp.append("v")
    if x == 23:
        exp.append("w")
    if x == 24:
        exp.append("x")
    if x == 25:
        exp.append("y")
    if x == 26:
        exp.append("z")
    if x == 27:
        exp.append(" ")
    if x == 28:
        exp.append("_")

print(exp)
```

It prints out the following.

```
['w', 'e', 'l', 'l', ' ', 't', 'h', 'e', ' ', 'f', 'l', 'a', 'g', ' ', 'i', 's', ' ', 'h', 'i', 'd', 'd', 'e', 'n', ' ', 'h', 'e', 'r', 'e', ' ', 'b', 'u', 't', ' ', 'f', 'i', 'r', 's', 't', ' ', 'w', 'e', ' ', 'h', 'a', 'v', 'e', ' ', 's', 'o', 'm', 'e', ' ', 't', 'e', 'x', 't', ' ', 't', 'o', ' ', 'c', 'o', 'n', 'f', 'u', 's', 'e', ' ', 'y', 'o', 'u', ' ', 'n', 'o', 'w', ' ', 't', 'h', 'e', ' ', 'f', 'l', 'a', 'g', ' ', 'i', 's', ' ', 'i', 'n', ' ', 'f', 'a', 'c', 't', ' ', 's', 'e', 'c', 'r', 'e', 't', 's', '_', 'a', 'r', 'e', '_', 'h', 'i', 'd', 'd', 'e', 'n', '_', 'i', 'n', '_', 't', 'h', 'i', 's', '_', 'l', 'i', 's', 't', ' ', 'd', 'o', 'n', 't', ' ', 'i', 'n', 'c', 'l', 'u', 'd', 'e', ' ', 't', 'h', 'e', ' ', 'p', 'a', 'r', 't', 's', ' ', 't', 'h', 'a', 't', ' ', 'a', 'r', 'e', ' ', 's', 'e', 'p', 'e', 'r', 'a', 't', 'e', 'd', ' ', 'w', 'i', 't', 'h', ' ', 's', 'p', 'a', 'c', 'e', 's']
```

Which says "well the flag is hidden here but first we have some text to confuse you now the flag is in fact secrets_are_hidden_in_this_list dont include the parts tha are seperated with spaces"

Tha flag is: secrets_are_hidden_in_this_list