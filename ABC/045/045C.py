import sys
from io import StringIO
import unittest

def resolve():
    S = input()
    combination = 2 ** (len(S) - 1)

    ans = 0
    for i in range(combination):
        # 2進数に直す
        bin_str = bin(i)[2:]

        # 上の桁分を埋める
        bin_str = '0' * (len(S) - len(bin_str) - 1) + bin_str

        formula = ''
        for i, s_char in enumerate(S):
            # 0の場合はなし、1の場合は'+'を入れて計算させる
            plus = ''
            if len(S) - 1 != i and bin_str[i] == '1':
                plus = '+'

            formula += s_char + plus

        # 文字列から計算する
        ans += eval(formula)

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
        input = """125"""
        output = """176"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """9999999999"""
        output = """12656242944"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()