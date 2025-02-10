''' 1. program for pyramid  '''

def pyramid_asc_program(a):
     for x in range(a):
         for y in range(x+1):
             print('*',end='')
         print()


def pyramid_dsc_program(a):
    for x in range(a):
        for y in range(x,a):
            print('*', end='')
        print()

def replace_string_with_char():
    s='aobocodo'
    count=1
    ss=s
    for x in s:
        if x=='o':
            new='&'*count
            ss = ss.replace(x, new,1)
        count+=1
    print(ss)

def count_repeated_char(s):
    result={x:s.count(x) for x in s}
    print(result)

def return_second_largest_number(n):
    x=sorted(n)
    print(x[-2])

def sorting_list(n):
    for x in range(len(n)):
        for y in range(len(n)):
            if n[x]>n[y]:
                n[x],n[y]=n[y],n[x]
    print(n)

def find_domain(n):
    import re
    pattern=r'@(\w+)\.'
    m=re.search(pattern,n)
    print(m.group(1))

def high_marks_in_dict():
    names = ['prem', 'kumar', 'john']
    marks = [11, 22, 33]
    name_marks=dict(zip(names,marks))
    print(name_marks)

class Parent(object):
    x = 1
class Child1(Parent):
    pass
class Child2(Parent):
    pass
print( Parent.x, Child1.x, Child2.x)
Child1.x = 2
print (Parent.x, Child1.x, Child2.x)
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)

def get_char_only(n):
    import re
    pattern=r'[^a-zA-Z]'
    a=re.sub(pattern,"",n)
    print(a)

def get_number_only(n):
    import re
    pattern=r'\d'
    a=re.findall(pattern,n)
    print(a)

def reverse_number(n):
    a=str(n)
    print(a[::-1])




