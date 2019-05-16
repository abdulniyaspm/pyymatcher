from heapq import nlargest
from collections import deque

try:
    from accel import longest_common_substring
except ImportError:
    raise RuntimeError("Unable to import the extension")


class PyyMatcher(object):
    """
    Class for calculating the similarity of two string objects.

    Usage: 
    >>> obj = PyyMatcher('Word1', 'word1')
    >>> obj.ratio()
    0.8
    >>> obj.ratio(case_insensitive=True)
    1.0
    >>> obj.longest_common_substr
    'ord1'
    """

    def __init__(self, s1, s2):
        self._s1 = s1
        self._s2 = s2

    def ratio(self, *, case_insensitive=False):
        o1, o2 = (
            (self._s1.lower(), self._s2.lower())
            if case_insensitive
            else (self._s1, self._s2)
        )
        total_len = (o1 + o2).__len__
        _stack = deque()
        _score = 0
        while True:
            large_string, left1, left2, right1, right2 = longest_common_substring(
                o1, o2
            )
            if large_string:
                _score += 2 * len(large_string)
            if right1 and right2:
                _stack.appendleft((right1, right2))
            if left1 and left2:
                _stack.appendleft((left1, left2))
            try:
                o1, o2 = _stack.popleft()
            except IndexError:
                return round(_score / total_len(), 10)

    @property
    def longest_common_substr(self):
        large_string, _, _, _, _ = longest_common_substring(self._s1, self._s2)
        return large_string

    def __repr__(self):
        return f"{self.__class__.__name__}({self._s1!r}, {self._s2!r})"

    __str__ = __repr__


def get_close_matches(
    *, word, possibilities, n=3, cutoff=0.6, case_insensitive=False
):  # Similar to the `difflib.get_close_matches`

    if not n > 0:
        raise ValueError("n must be > 0: %r" % (n,))
    if not 0.0 <= cutoff <= 1.0:
        raise ValueError("cutoff must be in [0.0, 1.0]: %r" % (cutoff,))

    if not all(isinstance(i, str) for i in possibilities):
        raise TypeError("possibilities must be sequence of strings")

    result = []
    for x in possibilities:
        s = PyyMatcher(word, x)
        if s.ratio(case_insensitive=case_insensitive) >= cutoff:
            result.append((s.ratio(case_insensitive=case_insensitive), x))
    result = nlargest(n, result)
    return [x for score, x in result]
