def zad_2_10(line):
    return len(line.split())


def zad_2_11(line):
    return ''.join(word + "_" for word in line.split())[:-1]


def zad_2_12(line):
    return ''.join(word[0] for word in line.split()), ''.join(word[-1] for word in line.split())


def zad_2_13(line):
    return sum(len(word) for word in line.split())


def zad_2_14(line):
    word = sorted(line.split(), key=len)[-1]
    return word, len(word)


def zad_2_15(L):
    return ''.join(str(l) for l in L)


def zad_2_16(line):
    return line.replace("GvR", "Guido van Rossum")


def zad_2_17(line):
    return sorted(line.split()), sorted(line.split(), key=len)


def zad_2_18(x):
    return  str(x).count('0')


def zad_2_19(L):
    return ''.join(str(num).zfill(3) + ',' for num in L)


if __name__ == '__main__':
    line = "Ala ma kota i psa GvR"
    L = [1, 12, 123, 12, 3]
    x = 10020304

    print("zad_2_10 : ", zad_2_10(line))
    print("zad_2_11 : ", zad_2_11(line))
    print("zad_2_12 : ", zad_2_12(line))
    print("zad_2_13 : ", zad_2_13(line))
    print("zad_2_14 : ", zad_2_14(line))
    print("zad_2_15 : ", zad_2_15(L))
    print("zad_2_16 : ", zad_2_16(line))
    print("zad_2_17 : ", zad_2_17(line))
    print("zad_2_18 : ", zad_2_18(x))
    print("zad_2_19 : ", zad_2_19(L))
