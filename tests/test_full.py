import pytest
import seval

def test_full():
    d = """[
        '1',
        b'b',
        (1 + 2, 1 / 5, 3 ** 8),
        { 'help': {'1', 'x', 1 + 2}, 1 : 'yelp' }
    ]"""
    assert seval.safe_eval(d) == eval(d)
