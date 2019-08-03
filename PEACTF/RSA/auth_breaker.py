n = 59883006898206291499785811163190956754007806709157091648869
e = 65537
c = 23731413167627600089782741107678182917228038671345300608183
m = pow(c, e, n)
#I cut 0x and L off of m, in order to convert it into ascii
hex = hex(m)[2:]
hex = hex[:-1]
print hex.strip().decode('hex')

#The second half of the flag is 1ng1sfun}