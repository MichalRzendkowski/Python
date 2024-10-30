# ZADANIE 4.2
def make_ruler(n):
    s = f'|{''.join("....|" for i in range(n))}'
    s += f'\n0{''.join(str(i + 1).rjust(5) for i in range(n))}'
    return s


def make_grid(rows, cols):
    s = ''
    for i in range(rows+1):
        s += '+' + ''.join(['---+' for i in range(cols)])
        if i != rows:
            s += '\n|' + ''.join(['   |' for i in range(cols)]) + '\n'
    return s


# ZADANIE 4.3
def factorial(n):
    f = 1
    for i in range(1, n+1): f *= i
    return f


# ZADANIE 4.4
def fibonacci(n):
    f1, f2 = 1, 1
    for i in range(n-1): f1, f2 = f2, f1 + f2
    return f1


# ZADANIE 4.5
def odwracanie(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
    return L


def odwracanie_rekurencyjne(L, left, right):
    if left >= right: return L
    L[left], L[right] = L[right], L[left]
    return odwracanie_rekurencyjne(L, left+1, right-1)


# ZADANIE 4.6
def sum_seq(sequence):
    sum = 0
    for element in sequence:
        if isinstance(element, (list, tuple)): sum += sum_seq(element)
        else: sum += element
    return sum


# ZADANIE 4.7
def flatten(sequence):
    flat = []
    for element in sequence:
        if isinstance(element, (list, tuple)): flat += flatten(element)
        else: flat.append(element)
    return flat


# Sprawdzanie wyników
if __name__ == '__main__':
    assert odwracanie([1, 2, 3, 4, 5], 1, 3) == [1, 4, 3, 2, 5]
    assert sum_seq([1,(2,3),[],[4,(5,6,7)],8,[9]]) == 45
    assert flatten([1,(2,3),[],[4,(5,6,7)],8,[9]]) == [1,2,3,4,5,6,7,8,9]
  
