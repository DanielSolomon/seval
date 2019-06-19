import ast

from .evalable import Evalable

class Arithmetic(
    metaclass       = Evalable, 
    evalable_nodes  = (
        ast.Num,
        ast.UnaryOp,
        ast.BinOp,
    ),
):

    _NUM_TYPES = (
        int,
        float,
        complex,
    )

    @classmethod
    def num(cls, node: ast.Num):
        yield node.n

    @classmethod
    def unaryop(cls, node: ast.UnaryOp):
        yield node.operand
        operand = yield
        if not isinstance(operand, cls._NUM_TYPES):
            raise ValueError('unsupported operand type')

        if isinstance(node.op, ast.UAdd):
            yield + operand

        elif isinstance(node.op, ast.USub):
            yield - operand

        # Invert case
        else: 
            if isinstance(node.op, complex):
                raise ValueError('unsupported operand for complex type')
            yield ~ operand

    @classmethod
    def binop(cls, node: ast.BinOp):
        yield node.left
        left = yield 
        yield node.right
        right = yield

        if not isinstance(left, cls._NUM_TYPES) or not isinstance(right, cls._NUM_TYPES):
            raise ValueError('unsupported type')

        op = node.op
        
        if isinstance(op, ast.Add):
            yield left + right

        elif isinstance(op, ast.Sub):
            yield left - right

        elif isinstance(op, ast.Mult):
            yield left * right

        elif isinstance(op, ast.Div):
            yield left / right

        elif isinstance(op, ast.FloorDiv):
            yield left // right

        elif isinstance(op, ast.Mod):
            yield left % right

        elif isinstance(op, ast.Pow):
            yield left ** right

        elif isinstance(op, ast.LShift):
            yield left << right

        elif isinstance(op, ast.RShift):
            yield left >> right

        elif isinstance(op, ast.BitAnd):
            yield left & right
        
        elif isinstance(op, ast.BitOr):
            yield left | right

        # ast.Xor
        else:
            yield left ^ right


