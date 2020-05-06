import pytest
from code import times_table

def test_answer():
    assert times_table.times_table(8) == [8, 16, 24, 32, 40, 48, 56, 64, 72, 80] 