# Protocol

## Challenge

'Alice sends a message to Bob saying to meet her somewhere. But Keith sees it, too, and goes to the place. Bob is delayed, and Alice and Keith meet.

Alice thinks Keith isn't good enough at CS to have found out that Alice and Bob were meeting there, but Keith argues that Alice sends secrets through a very insecure method. So, to prove it, Keith asks you to find out where Alice and Bob met, with your only prior knowledge being that it somehow involved [BunSpace](http://206.189.179.133/). See if you can find out where Alice met Bob.'

## Process
I used an sql injection to get into the website. I typed "or""=" into both the username and password spaces.I then searched 'posts' and clicked on Alice. I then right clicked the page and viewed the page source to find the flag as the location in a comment.

The flag is: flag{1.3521N_103.8198E}