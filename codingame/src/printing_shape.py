'''
So, we have a number input and printing output:

in: 
    1
out:
    * *


in: 
    2
out:
       *   *
    ** * * *

in: 
    3
out:
       *       *
       * *   * *
    ** * * * * *


in: 
    4
out:
         *           * 
         * *       * *
         * * *   * * *
    **** * * * * * * * 

'''

def print_shape(n):

    if n == 1:
        return ['* *']
    
    tmp = []
    
    last_row = f'{"* " * (n - 1)}*{" *" * (n - 1)}'
    last_row_spaces_len = len(last_row)

    starting_spaces = " " * (n + 1)
    for x in range(1, n):
        first = f'{"* " * x}'
        end = f'{" *" * x}'
        spaces = last_row_spaces_len - (len(first) * 2)
        tmp.append(f'{starting_spaces}{first}{" "*spaces}{end}')
    
    tmp.append(f'{"*" * n} {last_row}')
    return tmp


expected = ['* *']
result = print_shape(1)
assert result == expected, result

expected = ['   *   *', '** * * *']
result = print_shape(2)
assert result == expected, result


expected = ['    *       *', '    * *   * *', '*** * * * * *']
result = print_shape(3)
assert result == expected, result


expected = ['     *           *', '     * *       * *', '     * * *   * * *', '**** * * * * * * *']
result = print_shape(4)
assert result == expected, result
