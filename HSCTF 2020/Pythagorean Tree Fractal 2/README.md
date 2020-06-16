# Pythagorean Tree Fractal 2

## Challenge

"Because every good thing must have a sequel ;)

Please see the attached file for more details (and ignore the red dots on the images).

Note Don't worry about overlapping squares!"

You can download the problem files here [PTF2.pdf](PTF2.pdf)

## Process

The PDF asks you "If the square in Stage 1 has an area of 70368744177664, what is the area of the Stage 25 tree?". The squares added in every stage form isosceles right triangles with the previous squares. If you let the area stage 1 equal 4, its sides will be 2 and 2. As a result the side lengths of the sqares added in stage 2 must be sqrt(2) to be consistent with the pythagorean theorum. (sqrt(2) * sqrt(2)) * 2 squares = 4. 

This means each stage adds the same area of squares. Therefore the area of stage 25 is 70368744177664 * 25 which equals 1759218604441600.

The flag is flag{1759218604441600}