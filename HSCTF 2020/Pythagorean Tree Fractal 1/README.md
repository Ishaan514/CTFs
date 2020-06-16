# Pythagorean Tree Fractal 1

## Challenge

"Please see the attached file for more details (and ignore the red dots on the images)."

You can download the problem files here [Pythagorean_Tree_Fractal.pdf](Pythagorean_Tree_Fractal.pdf)

## Process

The PDF asks you "How many rectangles will Stage 50 include?" Each stage 2^n rectangles are added to the fractal. I wrote [this](Fractal.py) simple python program to calculate the resulting number of rectangles.

```
s = 0
for i in range(50):
	s += 2**i	
print s
```

The flag is flag{1125899906842623}.