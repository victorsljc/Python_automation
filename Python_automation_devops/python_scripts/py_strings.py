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

# >>>>>>>>>>>>>>>>>>>>>>  REG FUNCTIONS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''
Regular expressions (regex) are a powerful tool for pattern matching and text manipulation in Python.
They are widely used in QA automation for tasks like:

    1.Validating input data (e.g., emails, phone numbers)

    2.Extracting specific information from logs or responses

    3.Searching and replacing text

    findall	 ->   Returns a list containing all matches
    search	 ->   Returns a Match object if there is a match anywhere in the string
    split	 ->   Returns a list where the string has been split at each match
    sub	     ->   Replaces one or many matches with a string

1. re.match()
    Checks if the pattern matches at the beginning of the string.
    re.match(pattern, string, flags=0)
2. re.search()
    Searches for the pattern anywhere in the string.
    re.search(pattern, string, flags=0)
3. re.findall()
    re.findall(pattern, string, flags=0)
    Returns all non-overlapping matches of the pattern in the string as a list.
4. re.finditer()
    re.finditer(pattern, string, flags=0)
    Returns an iterator yielding match objects for all non-overlapping matches.
5. re.sub()
    re.sub(pattern, repl, string, count=0, flags=0)
    Replaces all occurrences of the pattern in the string with a replacement string.

Common Regex Patterns
        Digits: \d
        Word Characters: \w (letters, digits, underscore)
        Whitespace: \s
        Any Character: .
        Start of String: ^
        End of String: $
        Quantifiers:
        *: 0 or more [Use * when the preceding element is optional or can appear multiple times.]
        +: 1 or more [Use + when the preceding element must appear at least once.]
        ?: 0 or 1
        {n}: Exactly n times
        {n,}: n or more times
        {n,m}: Between n and m times
        ^   : starts with
        $   : ends with 
        []	: A set of characters [Used to specify a set of characters that can match at a particular position in the string.]
            Key Features
                Single Character Match:
                    Matches one character from the set inside the brackets.
                        Example: [abc] matches a, b, or c.

                Ranges:
                    Use a hyphen (-) to specify a range of characters.
                        Example: [a-z] matches any lowercase letter.

                Negation:
                    Use ^ at the beginning of the character class to negate it.
                        Example: [^abc] matches any character except a, b, or c.
                Special Characters:
                        Most special characters (e.g., ., *, +) lose their special meaning inside [].
       
        ()  : capture and grouping  
'''

def test_re_match():
    import re
    result = re.match('^world','hello world')
    if result :
        print(result.group())
    else:
        print('no match')

def test_re_search():
    import re
    result = re.search('world','this is the world and the bad world')
    print(result.group())

def test_re_find_all():
    import re
    result = re.findall('world','this is the world where bad worldly people leave')
    print(result)

def test_re_find_iter():
    import re
    s='this is the world where bad worldy=ly people live'
    result=re.finditer('world',s)
    for x in result:
        print(x.group(),'at position',x.start())

def test_re_sub():
    import re
    result = re.sub('\d+','X','there are 3 apples and 4 bananas')
    print(result)

def test_verify_email():
    import re
    email = "test@example.com"
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern, email):
        print("Valid email")
    else:
        print("Invalid email")

def test_extract_phone_number():
    import re
    text = "Contact us at 123-456-7890 or 987.654.3210."
    pattern= r'\d{3}+[-.]+\d{3}+[-.]+\d{4}'
    phone_numbers=re.findall(pattern,text)
    print(phone_numbers)

def test_replace_multitple_spaces():
    import re
    text= 'this   is    a    text'
    pattern=r'\s+'
    print(re.sub(pattern,' ',text))

def test_extract_url():
    import re
    text = "Visit https://example.com or http://test.org."
    pattern = r"https?://[^\s]+"
    urls = re.findall(pattern, text)
    print(urls)

def test_remove_digit_and_special_char_from_string():
    a = 'this is ba3234la vee3ra234nja3232neya;'
    pattern = r'[^0-9;]'
    import re
    print(''.join(re.findall(pattern, a)))















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