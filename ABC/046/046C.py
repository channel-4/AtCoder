import sys
from io import StringIO
import unittest

def resolve():
    import math as m

    N = int(input())
    # 初回は単純に人数として加算
    T, A = map(int, input().split())

    for _ in range(N - 1):
        t_i, a_i = map(int, input().split())

        # 比率を考えると総人数は T, A = n*t_i, n*a_i の形になる
        # 必ず現在のT, A以上となるnの値を考える
        n = max(-(-T // t_i), -(-A // a_i))

        # 更新
        T, A = n * t_i, n * a_i

    print(T + A)

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
        input = """3
2 3
1 1
3 2"""
        output = """10"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """4
1 1
1 1
1 5
1 100"""
        output = """101"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """5
3 10
48 17
31 199
231 23
3 2"""
        output = """6930"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()