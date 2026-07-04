import pytest

def test_thrid():
    assert 1 + 1 == 2

class TestThird:
    def test_third_string_comparison(self):
        assert "hello" == "hello"
        assert "za" in "zane"
        assert "test" != "testing"
        print("The test_third_string_comparison method has been executed successfully.")
    
    def test_third_float_comparison(self):
        assert 3.14 == 3.14
        assert 2.71 < 3.0
        assert 1.0 != 1.1
        result = 5.0 / 2.0
        assert pytest.approx(result) == 2.5555
        print("The test_third_float_comparison method has been executed successfully.")