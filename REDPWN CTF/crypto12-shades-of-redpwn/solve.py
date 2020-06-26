num12s = ['86','90','81','87','a3','49','99','43','97','97','41','92','49','7b','41','97','7b','44','92','7b','44','96','98','a5']
flagLetters = []
flag = ''
for num12 in num12s:
	flagLetters.append(chr(int(num12,12)))
for letter in flagLetters:
	flag = flag + letter
print flag

#flag{9u3ss1n9_1s_4n_4rt}