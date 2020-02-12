import sys
from io import StringIO
import unittest

def resolve():
    W = input()
    alpha = []
    num   = []
    for char in W :
        if char in alpha:
            num[alpha.index(char)] += 1
        else :
            alpha.append(char)
            num.append(1)

    ans = 'Yes'
    for n in num :
        if n % 2 == 1 :
            ans = 'No'

    print(ans)

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
        input = """abaccaba"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """hthth"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()