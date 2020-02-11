import sys
from io import StringIO
import unittest

# MEMO 制約的に2重forでいけるが計算量少ないいい方法が気になる
def resolve():
    N = int(input())
    a = list(map(int, input().split()))

    ans = float('INF')
    for i in range(-100, 101) :
        sum = 0
        for n in range(N) :
            sum += (a[n] - i)**2

        ans = min(ans, sum)

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
        input = """2
4 8"""
        output = """8"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3
1 1 3"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """3
4 2 5"""
        output = """5"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """4
-100 -100 -100 -100"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()