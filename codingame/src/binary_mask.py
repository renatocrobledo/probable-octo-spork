'''

    A bunch of '?' symbols are going to be received in a single string, so the point here is print a binary sequence depending of the number of symbols, 
    but not only that, there could be some binary numbers in the string too, so it should be printed at the received position while printing this binary 
    list.. 
    for example:
    ----------------------------------
    in: '?'
    out: ['0', '1']
    ----------------------------------
    in: '??'
    out: ['00', '01', '10', '11']
    ----------------------------------
    in: '???'
    out: ['000', '001', '010', '011', '100', '101', '110', '111']
    ----------------------------------
    But here's the tricky part:

    in: '1?' 
    out: ['10','11']
    ----------------------------------
    in: '?10??'
    out: ['01000', '01001', '01010', '01011', '11000', '11001', '11010', '11011']

    if no '?' marks are received it will return the same input

    in: '01010'
    out: ['01010']


'''

import re

def binary_list(mask):

    reg_exp = mask.replace('?', '(1|0)')
    mask_regex = re.compile(reg_exp)
    len_mask = len(mask)
    max_number = 2 ** len_mask

    result = []

    for n in range(max_number):
        binary = (bin(n)[2:]).zfill(len_mask)
        
        if mask_regex.match(binary):
            result.append(binary)

    return result
