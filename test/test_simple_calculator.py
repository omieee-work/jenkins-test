from ..simple_calculator import add_two, sub_two
def test_add_two():
    assert add_two(3, 2) == 5

def test_sub_two():
    assert sub_two(3, 2) == 1