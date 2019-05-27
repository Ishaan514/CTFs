string = "zkdxmxkhvgofoqvyeccuxokfimbtyhrbkpougnvzbhseotymydwbadenbzxrzfanxetkvyiczvoybearnqszydnwhrjamlpcqfxi"
total = 0

for char in string:
	if char == "h":
		total = total + 1
	elif char == "s":
		total = total + 1
		total = total * 2
	elif char == "c":
		total = total + 1
		total = total * 3
	elif char == "t":
		total = total + 1
		total = total * 4
	elif char == "f":
		total = total + 1
		total = total * 5

print("The flag is: " + str(total))