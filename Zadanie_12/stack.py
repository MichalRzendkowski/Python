# ZADANIE 12.2 (STACK)

class Stack:

    def __init__(self, size=10):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementów na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full():
            raise IndexError
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        if self.is_empty():
            raise IndexError
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None    # usuwam referencję
        return data
    
import unittest

class TestStack(unittest.TestCase):
    
    def test_is_empty(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        s.push(1)
        self.assertFalse(s.is_empty())
        s.pop()
        self.assertTrue(s.is_empty())

    def test_is_full(self):
        s = Stack()
        for i in range(10):
            self.assertFalse(s.is_full())
            s.push(i)
        self.assertTrue(s.is_full())

    def test_push(self):
        s = Stack()
        for i in range(10): s.push(i)
        with self.assertRaises(IndexError): s.push(1)

    def test_pop(self):
        s = Stack()
        with self.assertRaises(IndexError): s.pop()
        for i in range(10): s.push(i)
        for i in range(10): self.assertEqual(s.pop(), 9 - i)


if __name__ == '__main__':
    unittest.main()
