from proj import chek_correct_arg, select_house, select_grade
import pytest

def test_select_house():
    assert select_house("creativity") == "Revenclaw"

def test_select_grade():
    assert select_grade(2005) == "Grade 13"

def test_chek_correct_arg():
    with pytest.raises(SystemExit):
        chek_correct_arg()