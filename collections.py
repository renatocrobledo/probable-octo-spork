'''
collections ides some useful enhancements to tuples, list & dictionaries

'''

import collections

def collection_counter():
    example = 'A B B C D D D A B C C C'
    c = collections.Counter(example)

    print(c) # Counter({' ': 11, 'C': 4, 'B': 3, 'D': 3, 'A': 2})

'''
    if there's no key in a 'normal' dictionary it would raise a KeyError
'''

def default_dict():
    d = collections.defaultdict(int) # define the type of the values so initialize won't be needed
    d['n'] += 1 
    print(d) # defaultdict(<class 'int'>, {'n': 1})
    print(d['n']) # 1


def deque_test():
    deque = collections.deque('abcdefg')

    d = deque
    '''
    >>> d.append('x')
    >>> d
    deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'x'])
    >>> d.appendleft('f')
    >>> d
    deque(['f', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'x'])
    >>> d.extend('vbn')
    >>> d
    deque(['f', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'x', 'v', 'b', 'n'])
    >>> d.rotate(1)
    >>> d
    deque(['n', 'f', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'x', 'v', 'b'])
    '''

    return deque



