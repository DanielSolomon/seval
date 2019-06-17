import ast
import typing

from .evalable import Evalable

class MathExp(Evalable):

    ALLOWED_NODES = (
        ast.Num,
        # Unary
        ast.UnaryOp,
        ast.UAdd,
        ast.USub,
        ast.Invert,
        # Binary
        ast.BinOp,
        ast.Add,
        ast.Sub,
        ast.Mult,
        ast.Div,
        ast.FloorDiv,
        ast.Mod,
        ast.Pow,
        ast.LShift,
        ast.RShift,
        ast.BitAnd,
        ast.BitOr,
        ast.BitXor,
    )

    def __init__(self, expr: typing.Union[str, ast.Expression]):
        if isinstance(expr, str):
            expr = self.compile(expr, expected=ast.Expression)
        assert isinstance(expr, ast.Expression)
        self.expr = expr

    def evalable(self):
        return self.allowed_nodes(self.expr.body, *self.ALLOWED_NODES)
