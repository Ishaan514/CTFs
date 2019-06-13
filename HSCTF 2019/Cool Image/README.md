# Cool Image

## Challenge

"My friend told me he found a really cool image, but I couldn't open it. Can you help me access the image?"
You can download the file for this problem here [cool.pdf](cool.pdf)

## Process

At first, if we try to open this file as a PDF, we are told that it will not open because it is damaged or the file tpe is not recognized. 

If we run the command file on the given file we can are told that this is not actually a PDF, but a PNG. Similarly if we open up the file in notepad++, the first line is ‰PNG which strongly implies that this file is a PNG.

![Running the command file on the file](Capture.JPG)

I just renamed the file from [cool.pdf](cool.pdf) to [cool.png](cool.png) and tried to view it. The new file, cool.png successfully opens and clearly displays the flag.

![opening up the new PNG file](cool.png)

The flag is hsctf{who_uses_extensions_anyways}.