
# Python 3 notes

## core builtins

https://docs.python.org/3/library/functions.html

```python
open
print
compile
eval
    eval(*str), 
exec
input
repr

bytearray
bytes

vars
dir
format

isinstance
callable
issubclass

zip
tuple  // immutable seq objtype
map
sorted
list
filter
frozenset
set
iter
reversed
slice

len
range
enumerate
breakpoint
hash
id
next

object
bin
oct
hex
int
chr
str
ord
ascii
bool
float
complex
dict

divmod
max
min
pow
round

all
any

@property
getattr
hasattr
delattr
type

@staticmethod
@classmethod
super
globals
locals
help
```
reference

- [cheatsheat](#https://gto76.github.io/python-cheatsheet)
- [builtin functions](https://docs.python.org/3/library/functions.html)

## -> Libraries you want to learn

```python3
hashlib
concurrent.futures
argparse
functools
numba jit compile
```

## -> Pip <version> and Python Environment debian

    which pip --- PATH?
    pip show PAK

    --user
    on ubuntu designates user instead of system pip or pip3 installation

## -> Modules and Packages

defining \_\_init__ and \_\_main__

## -> Variables

reverse, backwards

    array[::-1]

transpose array

    zip(*ARRAY)

## -> some bullshit need to sort

    abs(*int or *float) -->  return absolute value
    complex(*int1, *int2) --> return int1 + j*int2
    divmod(*int1, *int2) --> return modular division and remainder
    floating point
    
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


## modules

tqdm

    from tqdm import tqdm, trange
    import time
    for i in trange(int, desc="name of loop")
        time.sleep(1) 

msgpack - save data in binary
