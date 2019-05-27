# Stolen Sheets

## Challenge

'Keith finds a sheet of paper with the following items:

A Sheet of Paper
one	qzc
two	xwq
three	xbpcc
four	tqop
five	tsfc
six	gsn
seven	gcfcz
eight	cskbx
nine	zszc
ten	xcz
The flag will be the message "mrkcdpmsuimzstqrlg" decoded. '

## Process

I spent a long time trying to figure out the distances between the letters thinking that that was how the letters were ciphered. That was unsuccessful, so I tried plugging this into numerous online cipher decrypters. It turns out that this text was using a affine cipher where all letters are mapped to other letters based on a function. I Solved this encryption by putting mrkcdpmsuimzstqrlg into https://www.dcode.fr/affine-cipher.

The flag is: algebraicmanifolds