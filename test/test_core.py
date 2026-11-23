import pytest
from receiptsort import add

def test_add():
    result = add(1, 1)
    assert result == 2