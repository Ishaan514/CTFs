# OK

## Challenge

'After ranting at length to a friend, Keith receives a message consisting of a single letter: "K". Incensed at this low-effort response, he responds with "OK", to which his friend replies "KOOK." An astute individual, Keith identifies the pattern instigated by his friend: subsequent messages consist of Keith and his friend replacing each "K" with "OK" and "O" with "KO". Help Keith find how many sets of consecutive Os of length two or greater are in the message on the 1000 reply. The first message, "K", does not count as a reply. Give your answer mod 10^9 + 7.

To clarify what constitutes "sets of consecutive Os of length two or greater": 
KOKOOKOOOKOOOO - there are three sets of consecutive Ks of length two or greater in this string ("OO", "OOO", "OOOO"). '

## Process

There is a clear pattern in how to count consecutive Os of length two or greater in Keith's conversation with his friend. I start the range at three because the first two responses have no consecutive Os. 

OKKO == 0
KOOK == 1
0 => 10
1 => 01
next = !previous inverted + previous

Every four letter can be reduced to a single character, therefore we can just count the reductons.


I wrote [this](ok.py) python program in order to find this number based on the pattern.
```
total = 1
for i in range(3,1000):
#    print i
    if i % 2 == 0:
        total = total*2 - 1
    else:
        total = total*2 + 1

x = total % 1000000007
print 'The flag is: ' + str(x)
```
The flag is: 114737202
