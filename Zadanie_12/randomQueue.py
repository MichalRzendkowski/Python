import random

class RandomQueue:
    
    def __init__(self, size):
        self.items = []
        self.n = 0
        self.size = size

    def insert(self, item):   # wstawia element w czasie O(1)
        if self.is_full():
            raise IndexError
        self.items.append(item)
        self.n += 1

    def remove(self):    # zwraca losowy element w czasie O(1)
        if self.is_empty():
            raise IndexError
        self.n -= 1
        i = random.randint(0, self.n)
        self.items[i], self.items[-1] = self.items[-1], self.items[i]
        return self.items.pop()

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.n == self.size

    def clear(self):   # czyszczenie listy
        self.items = []
        self.n = 0

import unittest

class TestStack(unittest.TestCase):
    
    def test_insert(self):
        q = RandomQueue(10)
        for i in range(10): q.insert(i)
        with self.assertRaises(IndexError): q.insert(1)
        with self.assertRaises(IndexError): RandomQueue(0).insert(1)

    def test_remove(self):
        q = RandomQueue(10)
        with self.assertRaises(IndexError): q.remove()

        v = [i for i in range(10)]
        for i in v: q.insert(i)
        for i in range(10):
            k = q.remove()
            self.assertTrue(k in v)
            v.remove(k)

    def test_is_empty(self):
        q = RandomQueue(10)
        self.assertTrue(q.is_empty())
        q.insert(1)
        self.assertFalse(q.is_empty())

    def test_is_full(self):
        q = RandomQueue(10)
        for i in range(10):
            self.assertFalse(q.is_full())
            q.insert(i)
        self.assertTrue(q.is_full())

    def test_clear(self):
        q = RandomQueue(10)
        for i in range(5): q.insert(i)
        q.clear()
        self.assertTrue(q.is_empty())


if __name__ == '__main__':
    unittest.main()
