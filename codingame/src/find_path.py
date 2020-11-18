'''
given a target, find the path to it
starting with any node in a tree

'''





def give_me_the_path(tree, start, goal):

    def recurse(path, key, value):
        
        
        if value == goal:
            return f'{path}'

        if isinstance(value, dict):
            for _key in value.keys():
                p = f'{path}.{_key}' if path else _key
                r = recurse(p, _key, value[_key])
                if r != '':
                    return r

        return ''
    
    path = recurse('','', tree)

    _start = reversed(start.split('.'))

    for s in _start:
        if s in path:
            path = path.replace(f'{s}.', '')
        else:
            path = '../' + path

    return path


test_tree = {
    'one':{
        'fasf': {
            'eee': 1,
            'oo': 2
        },
        'xcxcx': {
            'zz':3,
            'aa':4
        }
    },
    'two':{
        'dsfa': 5,
        'cvzvz': 6
    }
}


r = give_me_the_path(test_tree, 'one.fasf.eee', 6)

assert r == '../../../two.cvzvz', r


r = give_me_the_path(test_tree, 'one.fasf.eee', 2)

assert r == '../oo', r