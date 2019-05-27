# Teacher Struggles

## Challenge

'Keith's Computer Science teacher tells Keith that he will let Keith practice for HSCTF during class if she can solve a problem. Keith's Computer Science teacher gives Keith the following string: 

"zkdxmxkhvgofoqvyeccuxokfimbtyhrbkpougnvzbhseotymydwbadenbzxrzfanxetkvyiczvoybearnqszydnwhrjamlpcqfxi"

and tells Keith that she must start with 0 and add one everytime she sees an "h," add one and then multiply by two everytime she sees an "s," add one and multiply by three everytime she sees a "c," add one and multiply by four everytime she sees a "t," and add one and multiply by five everytime she sees an "f." The answer to the problem will be the resulting integer. Can you help Keith solve the problem?'

## Process

We are told exactly what to do for this problem. For each letter in the string, do something specific to a total.

I wrote [this](Decoder.py) python program in order to do exactly what is asked.

```
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
```

The flag is: 29774315