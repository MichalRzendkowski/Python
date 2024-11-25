import random

class IterA:
    def __iter__(self):
        self.value = True
        return self

    def __next__(self):
        self.value = not self.value
        return int(self.value)
    

class IterB:
    def __iter__(self):
        return self

    def __next__(self):
        l = ["N", "E", "S", "W"]
        return l[random.randint(0, 3)]
    

class IterC:
    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        v = self.value
        if self.value == 6: self.value = 0
        else: self.value += 1
        return v


if __name__ == "__main__":
    a = iter(IterA())
    b = iter(IterB())
    c = iter(IterC())
    print([next(a) for i in range(10)])
    print([next(b) for i in range(10)])
    print([next(c) for i in range(10)])
  
