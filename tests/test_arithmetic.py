import pytest
import random
import seval

bin_ops = (
    '+',
    '-',
    '*',
    '/',
    '//',
    '%',
    '**',
    '<<',
    '>>',
    '&',
    '|',
    '^',
)

un_ops = (
    '+',
    '-',
    '~',
)

def _get_random_digit(non_zero: bool = False):
    low = 1 if non_zero else 0
    return random.randint(low, 10)

def _get_unary(op, n):
    return f'{op}({n})'

def _get_binary(op, l, r):  
    return f'({l}) {op} ({r})'

@pytest.mark.parametrize('number', [
    '10',
    '-10',
    '0',
    '-0',
    '0x100',
    '0b111',
    '0o7654',
])
def test_num(number):
    assert seval.safe_eval(str(number)) == eval(number)

@pytest.mark.parametrize('op', un_ops)
def test_unary(op):
    d   = _get_random_digit()
    exp = _get_unary(op, d)
    assert seval.safe_eval(exp) == eval(exp)

@pytest.mark.parametrize('op', bin_ops)
def test_binary(op):
    l   = _get_random_digit()
    r   = _get_random_digit(non_zero=True)
    exp = _get_binary(op, l, r)
    assert seval.safe_eval(exp) == eval(exp)

def _exp(count):
    if count == 0:
        return _get_random_digit(non_zero=True)
    func = random.choice([_get_binary, _get_unary])
    if func == _get_binary:
        op = random.choice(bin_ops)
        return _get_binary(op, _exp(count - 1), _exp(count - 1))
    else:
        op = random.choice(un_ops)
        return _get_unary(op, _exp(count - 1))

@pytest.fixture
def exp():
    return _exp(3)

def test_expression(exp):
    assert seval.safe_eval(exp) == eval(exp)

