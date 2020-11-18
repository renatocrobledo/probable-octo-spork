def abbr(s):
    string_list = list(s)

    first = string_list.pop(0)
    last = string_list.pop()

    return f'{first}{len(string_list)}{last}'

result = abbr('are')
assert result == 'a1e', result

result = abbr('Wizeline')
assert result == 'W6e', result