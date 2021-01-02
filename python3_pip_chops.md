
# Python 3 Chops

## -> Quick Reminders

```python
arrayname[::-1]  # reverse, backwards

zip(*ARRAY)  # transpose array

dir(object)  # see all attributes

[ (do x) for x in array if x==whatever]

lambda a,b: a+b
```

- [cheatsheat](#https://gto76.github.io/python-cheatsheet)
- [builtin functions](https://docs.python.org/3/library/functions.html)

---

## -> Useful Libraries

```python3
hashlib
concurrent.futures
argparse
functools
numba jit compile
```

---

## -> Pip on Ubuntu

```bash
which pip

pip show $PACKAGE

pip install $PACKAGE --user 
```

---
## -> Std Methods

```python
abs(*int or *float)     ### return absolute value
complex(*int1, *int2)   ### return int1 + j*int2
divmod(*int1, *int2)    ### return modular division and remainder
floating point

all(*iterable)    ### return bool if all elements are true
any(*iterable)    ### return true if any element is true
bool(#[x])        ### standard truth telling procedure
callable(*object) ### return true if object callable {ie class or instance}
enumerate(iterable, start=0)  ### range(iterable), object[]
    

ascii(object) ### return readable string of ascii codes
bin(*int)     ### convert integer to binary '0bxxxxxxx' format
hex()
oct()
bytearray()       ### return new byte array lenght of int in brackets
bytes()           ### return byte word
compile(source, filename, mode, flags=0, dont_inherit=False, 
    optimize=-1)  ###
id(object)        ###  int value of id

    
chr(*int)         ### integer to unicode point equivalent
del x.*attribute  ###
isinstance(obj)   ###
issubclass(obj)   ###
staticmethod()    ###
    

classmethod()     ### return class method of function??
dir()             ### list objects active in current sessionca
eval(*str)        ### execute variable name stored in passed in string  
exec()            ### dynamic execution of python code, parse string as python statements
help(__builtin__) ###  gives example of usage of python function
globals()         ### prints out contents of all global variables
locals()          ###
input('')         ### next line is read in as string, can store to variable
```

---
## Core Builtin Functions

https://docs.python.org/3/library/functions.html

```python
open
print
compile
eval
eval(*str)
exec
input
repr
```

```python
bytearray
bytes
```

```python
vars
dir
format
```

```python
isinstance
callable
issubclass
```

```python
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
```

```python
len
range
enumerate
breakpoint
hash
id
next
```

```python
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
```

```python
divmod
max
min
pow
round
```

```python
all
any
```

```python
@property
getattr
hasattr
delattr
type
```

```python
@staticmethod
@classmethod
super
globals
locals
help
```

---