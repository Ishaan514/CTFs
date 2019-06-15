#Script for The Real Reversal
#Look at the bits of the given file
reversed = open('reversed.txt', 'rb')
reversedBits = reversed.read()
#Reverse the bits of the given file and write a new one
bits = reversedBits[::-1]
outputText = open('fix_attempt_one.txt','wb')
outputText.write(bits)
reversed.close()
outputText.close()
print("Fixed the bits")

#This gives us Latin characters in fixed_attempt_one.txt, but the characters are reversed. We can tell by the strange punctuation. The challenge also says that someone reversed the file twice.
#After looking through the text I determined that "}niw_eht_rof_8ftu{ftcsh" is likely the flag reversed

#For some strange reason, no matter what I did the file wouldn't be read as ascii characters with the line below, so I made a workaround using input() and retyping the reversed flag. This may have something to do with the fact that the written text appears like its in a strange font of some kind. }niw_eht_rof_8ftu{ftcsh 
#flipped = open('fix_attempt_one.txt','r')

reversedCharacters = str(input("What characters need to be reversed?\n(the text from fix_attempt_one in quotes) \n"))
#Reverse the characters from the new file 
characters = reversedCharacters[::-1]
print("Fixed the characters")
print("The Flag is: " +  str(characters))

#The flag is hsctf{utf8_for_the_win}