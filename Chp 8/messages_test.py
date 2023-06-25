from pytest import mark

from messages import word_count


@mark.parametrize('qty, expected', [
    (1, '1 part'),
    (2, '2 parts')
])
def test_show_count(qty, expected) -> None:
    got = word_count(qty, 'part')
    assert got == expected


def test_show_count_zero() -> None:
    got = word_count(0, 'part')
    assert got == 'no parts'


def test_irregular() -> None:
    got = word_count(3, 'mouse', 'mice')
    assert got == '3 mice'
