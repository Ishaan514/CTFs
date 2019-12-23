# Kellen's Broken File

## Challenge

"Kellen gave in to the temptation and started playing World of Tanks again. He turned the graphics up so high that something broke on his computer!

Kellen is going to lose his HEAD if he can't open this file. Please help him fix this broken file."

You can download the problem file here [Kellens_broken_file.pdf](Kellens_broken_file.pdf)

## Process

The given file does not open as intended. The challenge description hints that we should look at the file header. 

```
1.3
%Äåòåë§ó ÐÄÆ
4 0 obj
<< /Length 5 0 R /Filter /FlateDecode >>
```

A PDF file header is %PDF-1.7. The given file did not have it. I added a PDF file header to the file and saved it. The [new file](flag.pdf) opened as intended and displayed the flag.

The flag is nactf{kn0w_y0ur_f1l3_h34d3rsjeklwf}