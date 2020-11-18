class Celcious_1:
    
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_farenheit(self):
        return (self.temperature * 1.8) + 32

'''
 Basic Class in which we can access temperature directly:

    >>> human = Celcious_1()
    >>> human.temperature
    0
    >>> human.temperature = 37
    >>> human.to_farenheit()
    98.60000000000001

'''

class Celcious_2:
    
    def __init__(self, temperature=0):
        self._temperature = temperature # underscore is used to denote private variables :) 

    def to_farenheit(self):
        return (self.temperature * 1.8) + 32
    
    # getter method
    def get_temperature(self):
        return self._temperature

    # setter method
    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError('Ups, that cold is not possible!')
        self._temperature = value


'''
    But then according to thermodynamics, the temperature of any object cannot reach below -273.15 degress Celcious (absolute zero)
    and we can acces to the temperature attribute very easily so oine approach to get that point could be adding getters and setters:

    But stills is possible to assign the temperature manually, because python by itself don't recognize private attributes...

    >>> h = Celcious_2()
    >>> h._temperature
    0
    >>> h._temperature = -300
    >>> h._temperature
    -300

'''
class Celcious_3:
    
    def __init__(self, temperature=0):
        self._temperature = temperature # underscore is used to denote private variables :) 

    def to_farenheit(self):
        return (self.temperature * 1.8) + 32
    
    # getter method
    def get_temperature(self):
        return self._temperature

    # setter method
    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError('Ups, that cold is not possible!')
        self._temperature = value

    temperature = property(get_temperature, set_temperature) # NOTE: this definition must be after the getter and setter if is before it won't work


'''
    
    Now, let's suppose that in our implementation we make a reference of the temperature attribute directly we would have to change it
    to the proper getter and setter, so we can go further and use a property object:

    >>> h = Celcious_3()
    >>> h.temperature = -300
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "properties.py", line 75, in set_temperature
        raise ValueError('Ups, that cold is not possible!')
    ValueError: Ups, that cold is not possible!
    
    Nice! now it will throw an exception if we assign a non expected value directly

    We can say now that:

    " the actual temperature value is stored in the private variable: _temperature
    the temperature attribute is a property object which provides an interface to this private variable "
'''   

class Celcious_4:
    
    def __init__(self, temperature=0):
        self._temperature = temperature # underscore is used to denote private variables :) 

    def to_farenheit(self):
        return (self.temperature * 1.8) + 32
    
    # getter method
    @property
    def temperature(self):
        return self._temperature

    # setter method
    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError('Ups, that cold is not possible!')
        self._temperature = value



'''
    Just to make things cleaner is possible to reuse the same name for the getter ans setter using 
    a the cool property decorator:

    >>> h = Celcious_4()
    >>> h.temperature = -300
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "properties.py", line 116, in temperature
        raise ValueError('Ups, that cold is not possible!')
    ValueError: Ups, that cold is not possible!
    >>> h.temperature = 300
    >>> h.temperature
    300
    >>> h.to_farenheit()
    572.0
'''

