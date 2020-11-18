'''
A mole is a unit used in chemistry that which is 6.022e23 times (the Avogadro constant) of an element, or 6022 billion of billions times. For example, a mole of water contains 6.022e23 times the water molecule. A mole of rize would be 6.022e23 times a grain of rice, or 6022 billion of billions times, which is enough to feed the whole world for years. A mole is nothing more than a synonym for a quantity, as pair is a synonym for a quantity of 2.

A friend of your asked you to write a program that will calculates the molar mass of a molecule. She explains to you, the one who never listened in chemistry courses, that the molar mass is the mass of one mole of that molecule. And the molar mass of the molecule is the sum of all the molar mass of each atom multiplied by the number of that kind of atom.

You're not interested by chemistry, but it's the perfect occasion to sharpen your programming skills. She needs that program soon, like in less than 15 min. Will you succeed ?

Input
    Line 1: An integer N for the amount of atoms with their molar mass.
    N next lines: Two values atom, which is the symbol of the atom in the periodic table, and molarMass, which is the molar mass of that given atom, with 3 digits precision.

    Line 2: The molecule to parse in order to calculate its molar mass.
    
    Output
    Line 1 : The molar mass of the molecule, with 3 digits precision, including trailing 0 if necessary.

Constraints
As in the periodic table, an atom can be composed of one or two letters.
The molecule to parse is guaranteed to be valid. No need to check for unknown atoms.

'''


import re 

def calculate_1():

    n = int(input())

    d = {}

    for i in range(n):
        atom, molar_mass = input().split()
        molar_mass = float(molar_mass)
        d[atom] = molar_mass

    molecule = input()

    whole = re.split(r'(\d+)',molecule)

    result = 0

    while len(whole):
        data = whole.pop(0)

        if data == '':
            continue

        if data in d: #its a molecule
            
            if len(whole) and whole[0].isnumeric():
                value = int(whole.pop(0))
                result += (d[data] * value)
            else:
                result += d[data]

        # maybe is a molecule mixed with another:
        else:

            data = list(data)
            
            while len(data):
                n = data.pop()

                if n.islower():
                    name = data.pop() + n
                    whole.insert(0, name)
                elif n != ' ':
                    whole.insert(0, n)

    return f'{result:.3f}'



