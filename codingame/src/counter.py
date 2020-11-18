'''
The goal of your program is to compress a N by N grid into one single line using run-length encoding.
The grid contains only the characters "A", "B" or "C".

Input
    A list containing string of N characters.
Output
    Consecutive characters of the same type are expressed as the count followed by the character.
    If the count is 1, it is omitted.
    Consecutive means either:
        - two characters next to each other on the same row
        - or one character at the end of a given row and another one a the start of the next row

'''

def run_len_encoding(data):

    res = []

    row = list("".join(data))
    count = 1
    tmp = row.pop(0)

    while len(row):
        tmp_2 = row.pop(0)
        
        if tmp == tmp_2:
            count += 1
            if len(row) == 0: 
                res += [str(count) if count > 1 else '*', tmp]    
        else:
            res += [str(count) if count > 1 else '*', tmp]

            if len(row) == 0:
                res += [tmp_2]
            count = 1
            tmp = tmp_2

    return "".join(res).replace('*', '')
