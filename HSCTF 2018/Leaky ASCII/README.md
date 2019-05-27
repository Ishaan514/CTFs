# Leaky ASCII

## Challenge

'Keith found an open port at nc shell.hsctf.com 10101 and it seems like there is a hidden message. Can you help Keith identify it?'

## Process
The first time I connected, all I could see where asterisks where the password was supposed to be. So I decided to send everything the connection sends into a txt file.

```
shell.hsctf.com 10101 > [leaky.txt](leaky.txt)
```

I then looked in leaky.txt to find the redacted password, now unredacted. It was 6Xrzjoioge7RlnSQJehIm1262dhfgBrE. I then sent the password back. I opened up the txt file again and I found the flag at the end.

The flag is: flag_{3ScaPE_C0De5_4_l1F3}

Below are the contents of [leaky.txt](leaky.txt)

```
Hello
Is anybody there?
Oh hello there. Listen, I need you to do me a favor
I need to leak a password, don't tell anyone
Sending in 3...
2...
1...
+-----------------------------------------------------+
|                                                     |
|  THE PASSWORD IS: 6Xrzjoioge7RlnSQJehIm1262dhfgBrE  |
|  THE PASSWORD IS: ********************************
|                                                     |
+-----------------------------------------------------+
Did you get the password?
I think the censors might have tried to block it
Tell me the password I sent you, I must make sure you got it
> Thanks. I found this written on a piece of paper:
 flag_{3ScaPE_C0De5_4_l1F3}
```