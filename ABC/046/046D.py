import sys
from io import StringIO
import unittest

def resolve():
    s = input()

    # ジャンケンの回数
    num = len(s)
    # gの個数
    g_len = s.count('g')
    # グーの数は半分以上
    g_num = -(-num // 2)

    # gに対してgを出す
    # 相手のグーが足りない場合はpに対して出さなきゃいけないので
    # 負の値を取り、それがそのまま回答に繋がる
    g_len -= g_num
    print(g_len)

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
        input = """gpg"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """ggppgggpgg"""
        output = """2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()