import pytest

def test_first():
    assert 1 + 1 == 2


def test_first_string_comparison():
    assert "hello" == "hello"
    assert "za" in "zane"

def test_second_string_comparison():
    assert "hello" == "hello"
    assert "ca" in "zane"