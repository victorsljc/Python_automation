
# 2nd problem
# Given input s = 'aobocodo'
# Expected output = ‘a&b&&c&&&d&&&&’
# Replace ‘o’ with ‘&’ and based on repeating ‘o’
def test_practiec():
    s = 'aobocodo'
    b=''
    count=1
    for x in s:
        if x == 'o':
            x= count*'&'
            count=count+1
        b=b+x
    print(b)

#. input_str =’ aobocodo’
#expected output = ‘a&b&c&d&’

def test_3_problem():
    input_str ='aobocodo'
    b=''
    for x in input_str:
        if x =='o':
            x ='&'
        b=b+x
    print(b)

#4. input = premkumar prem kumar and find the repeated chars
def test_4_problem():
    input = 'premkumar prem kumar'
    d={s:input.count(s) for s in input}
    print(d)

# get second highest number
def test_5_problem():
    s = [1, 2, 66, 3, 7, 4, 9, 22]
    for x in range(len(s)):
        for y in range(len(s)):
            if s[x]<s[y]:
                s[x],s[y]=s[y],s[x]
    print(s[-2])

# return domain name
def test_6_problem():
    s = 'asdf@gmail.com'
    import re
    pattern='@(\w+)'
    match=re.search(pattern,s)
    print(match.group(1))

