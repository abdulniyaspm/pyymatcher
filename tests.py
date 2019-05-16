import unittest
from pyymatcher import PyyMatcher, get_close_matches


class TestWithString(unittest.TestCase):
    def test_ratio(self):
        # https://github.com/python/cpython/blob/master/Lib/test/test_difflib.py
        sm = PyyMatcher('b' * 100, 'b' * 50 + 'a' + 'b' * 50)
        self.assertAlmostEqual(sm.ratio(), 0.995, places=3)

    def test_case_insensitive(self):
        sm = PyyMatcher('WORD', 'word')
        self.assertEqual(sm.ratio(case_insensitive=True), 1.0)

    def test_longest_common_substr(self):
        sm = PyyMatcher('Sequence', 'TestSequence')
        self.assertEqual(sm.longest_common_substr, 'Sequence')


class TestCloseMatches(unittest.TestCase):
    def setUp(self):
        self.word = 'this'
        self.possibilities = ['tthis', 'thhis', 'this', 'thiss']

    def test_with_n_equal_one(self):
        sm = get_close_matches(
            word=self.word, possibilities=self.possibilities, n=1)
        self.assertEqual(sm, ['this'])

    def test_with_n_equal_zero(self):
        with self.assertRaises(ValueError):
            get_close_matches(
                word=self.word, possibilities=self.possibilities, n=0)

    def test_with_possibilities_without_string(self):
        with self.assertRaises(TypeError):
            get_close_matches(word=self.word, possibilities=[1, 2])

    def test_with_case_insensitive(self):
        sm = get_close_matches(
            word=self.word, possibilities=self.possibilities + ['THIS'], n=2, case_insensitive=True)
        self.assertEqual(sm, ['this', 'THIS'])


if __name__ == "__main__":
    unittest.main()
