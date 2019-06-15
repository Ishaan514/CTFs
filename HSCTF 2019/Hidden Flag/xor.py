import pwn

#Xor the origional image
challpng = open("chall.png")
challpng = challpng.read()
fixed = pwn.xor(challpng, "invisible")

#Write the new image
fixedpng = open("fixed.png", "w")
fixedpng.write(fixed)
print("fixed.png has been created")