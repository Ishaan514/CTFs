# crypto12-shades-of-redpwn

## Challenge

"Everyone's favorite guess god Tux just sent me a flag that he somehow encrypted with a color wheel!

I don't even know where to start, the wheel looks more like a clock than a cipher... can you help me crack the code"

You can download the problem files here [color-wheel.jpg](color-wheel.jpg) [ciphertext.jpg](ciphertext.jpg)

## Process

First I opened up the given files.

Color-wheel

![color-wheel.jpg](color-wheel.jpg)

Ciphertext

![ciphertext.jpg](ciphertext.jpg)

The color wheel and the ciphertext have matching colors. The color wheel also has a color at every position of the clock. I labelled the color wheel like a clock.

![color-wheel numbers.jpg](color-wheel numbers.jpg)

Using the color wheel I then labelled the ciphertext with the color wheel clock numbers.

![ciphertext numbers.png](ciphertext numbers.png)

I obtained the following values, which I interpreted as base12 values.

```
86 912 81 87 103 49 99 43 97 97 41 92 49 711 41 97 711 44 92 711 44 96 98 105

86 9c 81 87 a3 49 99 43 97 97 41 92 49 7b 41 97 7b 44 92 7b 44 96 98 a5
```

I wrote this python script to convert these base12 values to ascii [solve.py](solve.py)

```
num12s = ['86','90','81','87','a3','49','99','43','97','97','41','92','49','7b','41','97','7b','44','92','7b','44','96','98','a5']
flagLetters = []
flag = ''
for num12 in num12s:
	flagLetters.append(chr(int(num12,12)))
for letter in flagLetters:
	flag = flag + letter
print flag

#flag{9u3ss1n9_1s_4n_4rt}
```

The flag is flag{9u3ss1n9_1s_4n_4rt}