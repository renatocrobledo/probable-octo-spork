inputA = int('00100011',2)  
inputB = int('00101101',2)
print(str(bin(inputA | inputB))[2:])

a = '00100011'
b = '00101101'

c = [ '1' if int(n) + int(b[i]) == 1 else '0' for i, n in enumerate(a) ]

print("".join(c))
