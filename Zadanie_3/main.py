def zad_3_3():
    print([i for i in range(31) if not i % 3 == 0])


def zad_3_4():
    while True:
        x = input()
        if x == 'stop' : break
        try: float(x)
        except ValueError: print("error")
        else: print(f'x = {1}; x^3 = {2}', x, pow(float(x), 3))        


def zad_3_5(n):
    s = f'|{''.join("....|" for i in range(n))}'
    s += f'\n0{''.join(str(i + 1).rjust(5) for i in range(n))}'
    print(s)


def zad_3_6(m, n):
    s = ''
    for i in range(m+1):
        s += '+' + ''.join(['---+' for i in range(n)])
        if i != m:
            s += '\n|' + ''.join(['   |' for i in range(n)]) + '\n'
    print(s)


def zad_3_8(a, b):
    return list(set(a) & set(b)), list(set(a) | set(b))


def zad_3_9(l):
    return [sum(a) for a in l]


def zad_3_10():
    keys = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    values = [1, 5, 10, 50, 100, 500, 1000]
    d = dict(zip(keys, values))
    d = {keys[i] : values[i] for i in range(len(keys))}
    d = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)])
    d = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    return d
