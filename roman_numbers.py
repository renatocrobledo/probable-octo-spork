'''
 Integer to Roman number transformer
'''



symbols = {
    '1': ['I', 'V'],
    '10': ['X', 'L'],
    '100': ['C', 'D'],
    '1000': ['M', 'V']
}

def int_to_roman(n):
    
    l = list(str(n))
    r = []

    unity = '1'
    for x in range(len(l)):
        
        low, high = symbols[unity]
        tmp = int(l.pop())
        
        if tmp < 4:
            r.append(low * tmp)
        elif tmp == 4:  
            r.append(low + high)
        elif tmp > 4 and tmp < 9:  
            r.append(high + (low * ( tmp - 5)))
        else: #tmp == 9:
            next_bucket = unity + '0'
            if not next_bucket in symbols:
                next_bucket = '10'

            next_low = symbols[next_bucket][0]
            r.append(low + next_low)
        
        if len(unity) < 4:
            unity += '0'
        else:
            unity = '10'

    return "".join(reversed(r))
    

result = int_to_roman(20)
assert result == 'XX', result

result = int_to_roman(21)
assert result == 'XXI', result

result = int_to_roman(30)
assert result == 'XXX', result

result = int_to_roman(30)
assert result == 'XXX', result

result = int_to_roman(1343)
assert result == 'MCCCXLIII', result

result = int_to_roman(500000)
assert result == 'D', result

result = int_to_roman(10000)
assert result == 'X', result

result = int_to_roman(3999999)
assert result == 'MMMCMXCMXCMXCIX', result
