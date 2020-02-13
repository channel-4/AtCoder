import sys
from io import StringIO
import unittest

def resolve():
    S = {'a': [], 'b': [], 'c': []}

    for char in ['a', 'b', 'c']:
        S[char] = [c for c in input()]

    # 今誰のターンか, 終了フラグ
    now = 'a'
    end = 0

    while end == 0:
        # もしもうカードがなければ終了
        if len(S[now]) == 0:
            print(now.upper())
            end = 1
        else:
            # 先頭を取得しnow更新, 文字を詰める
            now = S[now].pop(0)

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
        input = """aca
accc
ca"""
        output = """A"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """abcb
aacb
bccc"""
        output = """C"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()