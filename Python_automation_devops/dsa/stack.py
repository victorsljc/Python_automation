

def test_reverse_string():
    a = 'bala'
    b = list(a)
    c = []
    for x in range(len(b)):
        c.append(b.pop())
    print(''.join(c))

def test_reverse_array():
    a = [10, 11, 12, 13, 14]
    b = [a.pop(), a.pop(), a.pop(), a.pop()]
    print(b)

