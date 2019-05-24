#Converts num (in base 10) to base b
def conv(num,b):
    convStr = "0123456789abcdefghijklmnopqrstuvwxyz"
    if num<b:
        return convStr[num]
    else:
        return conv(num//b,b) + convStr[num%b]

file1 = open('Chopsticks', 'r')
line = str(file1.readlines())
smallib10 = 0
bigib10 = 0
l10 = 0
oneb10 = 0
exclaimb10 = 0

#Count each character
for letter in line:
    if letter == 'i':
        smallib10 = smallib10+1
    if letter == 'I':
        bigib10 = bigib10+1
    if letter == 'l':
        l10 = l10 + 1
    if letter == '1':
        oneb10 = oneb10 +1
    if letter == '!':
        exclaimb10 = exclaimb10 + 1

#Convert number of each character to desired bases
smallib2 = bin(smallib10)[2:]
bigib2 = bin(bigib10)[2:]
l2 = bin(l10)[2:]
oneb2 = bin(oneb10)[2:]
exclaimb2 = bin(exclaimb10)[2:]

smallib3 = str(conv(smallib10,3))
smallib4 = str(conv(smallib10,4))
smallib5 = str(conv(smallib10,5))
smallib6 = str(conv(smallib10,6))
smallib7 = str(conv(smallib10,7))
smallib8 = str(conv(smallib10,8))
smallib9 = str(conv(smallib10,9))

bigib3 = str(conv(bigib10,3))
bigib4 = str(conv(bigib10,4))
bigib5 = str(conv(bigib10,5))
bigib6 = str(conv(bigib10,6))
bigib7 = str(conv(bigib10,7))
bigib8 = str(conv(bigib10,8))
bigib9 = str(conv(bigib10,9))

l3 = str(conv(l10, 3))
l4 = str(conv(l10, 4))
l5 = str(conv(l10, 5))
l6 = str(conv(l10, 6))
l7 = str(conv(l10, 7))
l8 = str(conv(l10, 8))
l9 = str(conv(l10, 9))

oneb3 = str(conv(oneb10, 3))
oneb4 = str(conv(oneb10, 4))
oneb5 = str(conv(oneb10, 5))
oneb6 = str(conv(oneb10, 6))
oneb7 = str(conv(oneb10, 7))
oneb8 = str(conv(oneb10, 8))
oneb9 = str(conv(oneb10, 9))

exclaimb3 = str(conv(exclaimb10, 3))
exclaimb4 = str(conv(exclaimb10, 4))
exclaimb5 = str(conv(exclaimb10, 5))
exclaimb6 = str(conv(exclaimb10, 6))
exclaimb7 = str(conv(exclaimb10, 7))
exclaimb8 = str(conv(exclaimb10, 8))
exclaimb9 = str(conv(exclaimb10, 9))

#Find the flag
print "The flag is: " + str(len(str(smallib2)+str(smallib3)+str(smallib4)+str(smallib5)+str(smallib6)+str(smallib7)+str(smallib8)+str(smallib9)+str(smallib10)+str(bigib2)+str(bigib3)+str(bigib4)+str(bigib5)+str(bigib6)+str(bigib7)+str(bigib8)+str(bigib9)+str(bigib10)+str(l2)+str(l3)+str(l4)+str(l5)+str(l6)+str(l7)+str(l8)+str(l9)+str(l10)+str(oneb2)+str(oneb3)+str(oneb4)+str(oneb5)+str(oneb6)+str(oneb7)+str(oneb8)+str(oneb9)+str(oneb10)+str(exclaimb2)+str(exclaimb3)+str(exclaimb4)+str(exclaimb5)+str(exclaimb6)+str(exclaimb7)+str(exclaimb8)+str(exclaimb9)+str(exclaimb10)))
#The flag is: 274