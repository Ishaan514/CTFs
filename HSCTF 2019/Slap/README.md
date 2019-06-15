# Slap

## Challenge

"Don't get slapped too hard."

You can download the file for this problem here [slap.jpg](slap.jpg)

## Process

I opened the file and didn't find anything interesting.

![slap.jpg](slap.jpg)

I tried running strings on the image and using grep for the flag format.
```
$ strings slap.jpg | grep hsctf{
```

![Flag](Capture.JPG)

It was that simple. 

The flag is hsctf{twoslapsnonetforce}