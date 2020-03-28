import sys
from io import StringIO
import unittest

def resolve():
    s = input()

    s_first = s[0]
    s_last = s[-1]

    # 偶数の場合
    if (len(s) % 2 == 0):
        # a...a のような型 => 最終形は奇数
        if (s_first == s_last) :
            print('First')
        # a...b のような型 => 最終形は偶数
        else:
            print('Second')
    else:
        if (s_first == s_last):
            print('Second')
            # a...b のような型 => 最終形は偶数
        else:
            print('First')

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
        input = """aba"""
        output = """Second"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """abc"""
        output = """First"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """abcab"""
        output = """First"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()