
# Python 3 notes

- 


reference
- [cheatsheat](#https://gto76.github.io/python-cheatsheet)
- [builtin functions](https://docs.python.org/3/library/functions.html)

## -> Libraries you want to learn

```python3
hashlib
concurrent.futures
argparse
functools
```

## -> Python Environment

## -> Naming and Project Structure

## -> Exploring Objects

for obj
  try:
    dir(obj)
    

## -> Modules and Packages

defining \_\_init__ and \_\_main__

## -> Loops, control stuctures

pass like ignore me vs continue go to next loop loop

try except

## -> Variables

[decorators](#https://stackoverflow.com/questions/6392739/what-does-the-at-symbol-do-in-python)

    @functools

reverse, backwards

    array[::-1]

transpose array

    zip(*ARRAY)

other

    map()
    list
    zip

## -> Dictionaries

## -> Integers, Strings, Chars, other datatypes

---

## -> some bullshit need to sort

funcname = lambda argument_list: expression
funcname(args)


    abs(*int or *float) -->  return absolute value
    complex(*int1, *int2) --> return int1 + j*int2
    divmod(*int1, *int2) --> return modular division and remainder
    float(x) --> int, string, scientific to floating point
    max()
    min()
    str()
    sum()
    
    all(*iterable) --> return bool if all elements are true
    any(*iterable) --> return true if any element is true
    bool(#[x])  --> standard truth telling procedure
        callable(*object) --> return true if object callable {ie class or instance}
    enumerate(iterable, start=0)  --> range(iterable), object[]
    
    
    
    ascii(object) --> return readable string of ascii codes
    bin(*int)  --> convert integer to binary '0bxxxxxxx' format
    hex()
    oct()
        bytearray() --> return new byte array lenght of int in brackets
    bytes() --> return byte word
        compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)  -->
    id(object) -->  int value of id
    
    
    
    chr(*int) --> integer to unicode point equivalent
    del x.*attribute
    isinstance(obj)
    issubclass(obj)
    staticmethod()
    
    
    
    
    classmethod() --> return class method of function??
    dir() --> list objects active in current sessionca
        eval(*str)  --> execute variable name stored in passed in string  
        exec() --> dynamic execution of python code, parse string as python statements
        help(__builtin__) -->  gives example of usage of python function
    globals() --> prints out contents of all global variables
    locals()
        input('') --> next line is read in as string, can store to variable
    
    
    *zip() unzip a list
    zip() --> handy for double loop in a for
    vars(*dict)
    sum()
    sorted(x)
    reversed()
    next() --> return next item from iterator
    len(obj)
    hash()
    dict()
    set()
    list()  --> mutable seq type
    tuple()  --> immutable seq type
    collections module

# pip

    pip show PAK
    details about installed package

    --user
    on ubuntu designates user instead of system pip or pip3 installation
