keyChars = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~'

unfiltered = open('unfiltered.txt', 'r')
unfiltered_text = unfiltered.readlines()

stripped_text = []
for line in unfiltered_text:
	if line != 'Enter the password.\n' and line != 'welcome to the login portal.\n':
		line = line.strip('\n')
		stripped_text.append(line)

#print(stripped_text)
print "Text has been stripped"

flag = ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']

#print flag


for i in range(0,len(stripped_text)):
	line = stripped_text[i]
	for j in range(0,len(line)):
		char = line[j]
		if char == '1':
			flag[j] = keyChars[i]
#	print "Checking " + str(keyChars[i])
#			print flag
#print flag
print ("All letters have been checked")

temp = ''
for k in flag:
	temp = temp + str(k)

flag = temp
print('The flag is ' + flag)
#The flag is bcactf{y0u_4r3_4_m4573rm1nD!_Ym9vbGlu}

