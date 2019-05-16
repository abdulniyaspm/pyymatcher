# PyyMatcher

[![License](https://img.shields.io/pypi/l/pyymatcher.svg)](https://pypi.org/project/pyymatcher/)
[![Version](https://img.shields.io/pypi/v/pyymatcher.svg)](https://pypi.org/project/pyymatcher/)
[![Python versions](https://img.shields.io/pypi/pyversions/pyymatcher.svg)](https://pypi.org/project/pyymatcher/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

> Implementation of pattern matching in Python(using gestalt approach).
> This library implements the underlaying algorithm(longest_common_substring) with C++.

## Installation

```python
pip install pyymatcher
```

## Usage example

```python
>> from pyymatcher import PyyMatcher, get_close_matches

>>> obj = PyyMatcher('Word1', 'word1')
>>> obj.ratio()
0.8
>>> obj.ratio(case_insensitive=True)
1.0
>>> obj.longest_common_substr
'ord1'

>>> word = 'thiis'
>>> get_close_matches(word=word, 
                      possibilities=['tthis', 'thhis', 'this', 'thiss', 'THIS'], 
                      n=1)
['this']
>>> get_close_matches(word=word, 
                      possibilities=['tthis', 'thhis', 'this', 'thiss', 'THIS'], 
                      n=2, 
                      case_insensitive=True)
['this', 'THIS']
```

## Release History

* 0.0.1
    * initial release

## Support

Python 3.6+

## Meta

Abdul Niyas P M – [@AbdulNiyas19](https://twitter.com/AbdulNiyas19) – abdulniyaspm@gmail.com

Distributed under the MIT license. See ``LICENSE`` for more information.

[Github Profile](https://github.com/abdulniyaspm)

## Contributing

1. Fork it (https://github.com/abdulniyaspm/pyymatcher/fork)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

