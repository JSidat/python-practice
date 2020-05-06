import pytest
from code import Letter_count

def test_count():
    assert Letter_count.letter_count('banana', 'a') == 3