# Data Types
# complex - big numbers
# int
# float
def floatAndNumbers ():
    print(2 + 4); # Result: 6
    print(2 - 4); # Result: -2
    print(2 * 4); # Result: 8
    print(2 / 4); # Result: 0.5


    print(type(2 * 4)); # Result: <class 'int'>
    print(type(2 / 4)); # Result: <class 'float'>

    print(20 + 13.3); # Result: 33.3
    print(1.1 + 8.9); # Result: 10.0

    print(2 ** 3); # Result: 8

    print(2 // 4); # Result: 0 It's rounding down or up based on the rest.
    print(5 // 4); # Result: 1

    print(5 % 4); # Result: 1 It returns the remainder of the calculation


# Math Functions - functions which is applyable to number or float data types.
def numberMethod ():
    print(round(10.0)) # Result: 10
    print(round(10.0, 2)) # Result: 10.0
    print(round(10.0, 5)) # Result: 10.0

    print(abs(-20)) # Result: 20 / Returns the absolute number or argument.

# str
def stringTypes():
    print(type('text')); # Result: <class 'str'>

    # for long string you can use ''' 3 quotes
    test_text = ''' test 1
        test  2 
        test 3
    '''

    print(test_text)


    # string concatenations:
    print('hello '+'python') # hello python

    print('hello '+ 5) # ERROR: can only concatenate str (not "int") to str

def dataTypeConversion():
    num = 100
    print(type(num)) # <class 'int'>
    print(type(str(num))) # <class 'str'>


dataTypeConversion()

# bool
# list
# tuple
# set
# dict

#Classes

#None