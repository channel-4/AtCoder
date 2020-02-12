import sys
from io import StringIO
import unittest

def resolve():
    N, A = map(int, input().split())
    X = list(map(int, input().split()))

    # 0~N枚 => N+1, 合計の最大値はN*50
    dp = [[[0] * (N * 50 + 50) for _ in range(N + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 1

    # i枚目でk枚を選択、合計がk
    for i in range(N):
        for j in range(N):
            for k in range(N * 50):
                # 選択しない場合
                dp[i + 1][j][k] += dp[i][j][k]

                # 選択する場合
                dp[i + 1][j + 1][k + X[i]] += dp[i][j][k]

    ans = 0
    for i in range(1, N + 1):
        ans += dp[N][i][i * A]

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
        input = """4 8
7 9 8 9"""
        output = """5"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3 8
6 6 9"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """8 5
3 6 2 8 7 6 5 9"""
        output = """19"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """33 3
3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3"""
        output = """8589934591"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()