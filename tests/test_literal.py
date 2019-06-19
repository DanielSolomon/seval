import pytest
import seval

@pytest.mark.parametrize('literal', [
    '""',
    'b""',
    '[]',
    '{}',
])
def test_literal(literal):
    assert seval.safe_eval(literal) == eval(literal)


@pytest.mark.parametrize('seq', [
    [
        '1',
        'a',
        b'b',
        '-1',
    ]
])
def test_sequence(seq):
    for t in (list, set, tuple):
        assert seval.safe_eval(repr(t(seq))) == eval(repr(t(seq)))

def test_dict():
    d = {'a': 1, 'a b c': 2, 1: 'a'}
    assert seval.safe_eval(repr(d)) == d