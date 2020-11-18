m,a,b,r=input(),int(input(),2),int(input(),2),int(input(),2)
f={'AND':a&b,'OR':a|b,'XOR':a^b}
print(str(f[m]==r).lower())