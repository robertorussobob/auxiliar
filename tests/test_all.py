from auxiliar import are_all_the_same


def test_are_all_the_same():
    a = [0, 1]
    b = [0, 0]
    assert not are_all_the_same(a)
    assert are_all_the_same(b)
