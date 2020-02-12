import sys
from io import StringIO
import unittest

def resolve():
    N = int(input())
    K = int(input())
    X = int(input())
    Y = int(input())

    val = 0
    for i in range(N) :
        if i >= K :
            val += Y
        else :
            val += X

    print(val)

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """5
3
10000
9000"""
        output = """48000"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2
3
10000
9000"""
        output = """20000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()