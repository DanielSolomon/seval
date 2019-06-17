import ast
import typing

from .evalable import Evalable

class LiteralExp(Evalable):

    ALLOWED_NODES = (
        # Took from ast.literal_eval _convert function.
        ast.Constant,
        ast.Str,
        ast.Bytes,
        ast.Tuple,
        ast.List,
        ast.Set,
        ast.Dict,
        ast.NameConstant,
        ast.UnaryOp,
        ast.USub,
        ast.UAdd,
        ast.Invert,
        # Not from ast
        ast.Load,
        ast.Num,
    )

    def __init__(self, expr: typing.Union[str, ast.Expression]):
        if isinstance(expr, str):
            expr = self.compile(expr, expected=ast.Expression)
        assert isinstance(expr, ast.Expression)
        self.expr = expr

    def evalable(self):
        return self.allowed_nodes(self.expr.body, *self.ALLOWED_NODES)