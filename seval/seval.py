import abc
import ast
import typing

from .literal_exp   import LiteralExp
from .math_exp      import MathExp

EVALABLES = (
    LiteralExp,
    MathExp,
)

def safe_eval(s: str):
    for evalable in EVALABLES:
        try:
            e = evalable(s)
            if e.evalable():
                return eval(s)
        except AssertionError:
            pass
    raise ValueError(f'cannot evaluate {s} safely')