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

    # print('hello '+ 5) # ERROR: can only concatenate str (not "int") to str

    text = 'trol lololo olol'
    print(text[-1]) # Result: l
    print(text[0:5]) # Result: "trol "
    print(text[0:10]) # Result: "trol lolol "
    print(text[0:10:2]) # Result: "to oo"
    print(text[0:]) # Result: "trol lololo olol" -will return whole string because there is no stop argument
    print(text[:5]) # Result: "trol" -will return up to first 5 letters
    print(text[::-1]) # Result: will reverse the order!!!! REMEMBER

    print(len(text)) # Result: will return the length of string.

    # STRINGS ARE IMMUTABLE!

    print(text.upper()) # Result: TROL LOLOLO OLOL - everything in CAPS
    print(text.capitalize()) # Result: Trol lololo olol - capiutalize string
    print(text.find('r')) # Result: 1 - return index of first appearence
    print(text.replace('r', 'k')) # Result: tkol lololo olol - replace
    print(text.replace('lo', 'saasas')) # Result: trol saasassaasassaasas osaasasl - replace

def dataTypeConversion():
    num = 100
    print(type(num)) # <class 'int'>
    print(type(str(num))) # <class 'str'>


# bool
def boolTypes():
    print('Boolean: ', True, False)
    print(bool(123)) # True

# list
def listType():
    print('List: ', []) # []
    user_ids = [1, 2, 3, 4, 5]
    print('Last user id is: ', user_ids[-1]) # 5

    user_ids_copy = user_ids 
    user_ids_copy[0] = 'Test 1'

    # That operation changed the first item in both arrays because python created another variable which points to that memory address.

    print(user_ids) # ['Test 1', 2, 3, 4, 5]
    print(user_ids_copy) # ['Test 1', 2, 3, 4, 5]

    # If we need a full copy of an array we need to use [:]
    user_ids_copy = user_ids[:]
    user_ids_copy[0] = 'test213132312'
    print(user_ids) # ['Test 1', 2, 3, 4, 5]
    print(user_ids_copy) # ['test213132312', 2, 3, 4, 5]

def listMethods():
    array = [1, 2, 3, 4, 5]

    lastElementOfArray = array.pop() # 5
    firstElementOfArray = array.pop(0) # 1

    print(lastElementOfArray)
    print(firstElementOfArray)

    print(array) # [2, 3, 4] - Because pop removes and save the value from list

    array.insert(0, 1) # insert to the start
    array.insert(len(array), 5) # insert to the end

    print(array) # [1, 2, 3, 4, 5]

    array.append('test')

    print(array) # [1, 2, 3, 4, 5, 'test']

    array.remove(1) # removes the given element
    # array.remove(1213) # if value is not in array there will be an error: ValueError: list.remove(x): x not in list
    
    print(array)

    array.clear() # delete array items

    print(array) # []

    array = ['test', 'test2', 'test3'] # just some test data

    print(array.index('test2')) # 1

    
    # print(array.index('test2', 2)) # Error because there is a step 2 so it will jump throught our test2

    print('test' in array) # True - because 'test' is in array

    print(array.count('test')) # 1 - counts how many times 'test' is in array

    print(array.sort()) # None - because it first change the values and does not return the values.

    print(array) # [test1, test2, test3] - sorted array

    array2 = [2, 4, 1, 3]

    print(sorted(array2)) # [1, 2, 3, 4] - it didn't changed the array2, it created a copy and sorted that new copy.

    array2.reverse()

    print(array2) # 3, 1, 4,2 - it reversed the array

    a, *rest = array2
    print(a) # first element -  3 
    print(rest) # rest of the list -   [1,4,2]


# dict
def dictTypeAndMethods():
    user = {
        'name': 'Erik',
        'age': 23
    }

    print(user['name']) # key can be number | string | boolean
    
    print(user.get('age')) # Erik 
    print(user.get('test2')) # In case If there is no age then it will return None 

    print('secret_prop' in user) # False - a way to check if there is a dict property

    print('age' in user.keys()) # True - a way to check if there is a dict property
    print(user.items()) # tuple based key-values
    #user.clear()
    print(user) # {}

    userCopy = user.copy() # this is creating not an anchor but a full new object copy!

    print(userCopy)

dictTypeAndMethods()

# tuple
# set

#Classes

#None