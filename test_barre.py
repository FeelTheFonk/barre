import pytest
from barre import b
import io
import sys

def test_basic_iteration():
    assert list(b(range(3))) == [0, 1, 2]

def test_empty_iterable():
    assert list(b([])) == []

def test_string_iterable():
    assert list(b("abc")) == ["a", "b", "c"]

def test_output_format(capsys):
    list(b(range(1)))
    captured = capsys.readouterr()
    assert "[" in captured.out
    assert "]" in captured.out
    assert "1/1" in captured.out

def test_large_numbers():
    large_list = range(1000)
    result = list(b(large_list))
    assert len(result) == 1000
    assert result[0] == 0
    assert result[-1] == 999