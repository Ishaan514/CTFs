# Dexter's Lab

## Challenge

"Dee Dee,

Please check in on your brother's lab at dexterslab.web.2019.nactf.com We know his username is Dexter, but we don't know his password! Maybe you can use a SQL injection

Mom + Dad"

## Process

We can tell that this is a SQL injection challenge and that the username is Dexter from the challenge description. The using the Password: anything' OR 'x'='x and the Username: Dexter we can log in. 

Once logged in the message "Welcome Dexter. nactf{1nj3c7ion5_ar3_saf3_in_th3_l4b}" is displayed.

The flag is nactf{1nj3c7ion5_ar3_saf3_in_th3_l4b}