# converts string to upper case
from pandas.core.computation.common import result_type_many


def test_upper_case():
    a='rabit'
    print('\n',a.upper())

#converts string to lower case
def test_lower():
    a='RAJU'
    print('\n',a.lower())

# converts string like first letter is capital in string
def test_capitalize():
    a='hello world'
    print(a.capitalize())

# each word of first letter is capital
def test_title():
    a='hello world'
    print(a.title())

# removes white spaces
def test_strip():
    a='  hello world'
    print(a.strip())

# removes whitespace from left side of string
def test_lstrip():
    a='  hello world'
    print(a.lstrip())

# removes whitespaces from right side of string
def test_rstrip():
    a='  hello world  '
    print(a.rstrip())

# replaces string/literal with new string/literal
def test_replace():
    a='raju'
    print(a.replace('r','g'))

# splits a string based on separator
def test_split():
    a='raju rani bava'
    b='rani,raju,rah'
    c='rani.raju.rah'
    print(b.split(',')) # return type is list

#joins the string based on separator
def test_join():
    a='raju'
    print('-'.join(a)) # output - r-a-j-u

def test_find():
    a='raju'
    print(a.find('r')) # if char is there return char else returns -1
    print(a.find('g')) # returns -1

def test_index():
    a='gajini'
    print(a.index('g'))
    print(a.index('r')) # if char not there, throws value error

def test_starts_with():
    a='raju'
    print(a.startswith('r'))
    print(a.startswith('g')) # if char not starts with then returns false

def test_isalpha():
    a='raju'
    print(a.isalpha())

def test_isalpha_numeric():
    a='raju2'
    print(a.isalnum())

def test_isdigit():
    a='123'
    print(a.isdigit())

def test_islower():
    a='HELLO'
    print(a.islower())

def test_isupper():
    a='hello'
    print(a.isupper())

def test_count():
    a='hello'
    print(a.count('l'))

def test_format():
    name='raju'
    age=25
    a=10
    b=10
    # print("I am {} and I have {}".format(name,age))
    # print(f"I am {name} and I have {age}")
    print(f'the sum of {a} and {b} is {a+b}')

# it fills with 0s before the string
def test_zfill():
    a='10'
    print(a.zfill(3)) # return type is string

def  test_encode():
    a='raju'
    print(a.encode('utf-8'))

# swaps the case to opposite case liek upper -> lower, lower-> upper
def test_swapcode():
    a='HelloWorld'
    print(a.swapcase())

def reverse_string():
    a='raju'
    print(a[::-1])

def count_number_of_string_literals():
    a='rajuanna'
    b=sum([1 for char in a])
    print(b)

def test_remove_duplicates():
    a='adffaadfweete'
    b=''
    for x in a:
        if x in b:
            pass
        else:
            b=b+x
    print(b)

def test_digit_in_str():
    a='wer,13'
    for x in a:
        if '0'<=x<='9':
            pass
        else:
            print(x)