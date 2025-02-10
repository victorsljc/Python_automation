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