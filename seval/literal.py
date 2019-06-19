import ast

from .evalable import Evalable

_list   = list
_tuple  = tuple
_dict   = dict
_set    = set

class Literal(
    metaclass       = Evalable,
    evalable_nodes  = (
        ast.Constant,
        ast.Str,
        ast.Bytes,
        ast.Tuple,
        ast.List,
        ast.Set,
        ast.Dict,
        ast.NameConstant,
    ),
):

    @classmethod
    def constant(cls, node: ast.Constant):
        yield node.value

    @classmethod
    def str(cls, node: ast.Str):
        yield node.s

    @classmethod
    def bytes(cls, node: ast.Bytes):
        yield node.s

    @classmethod
    def tuple(cls, node: ast.Tuple):
        l = []
        for n in node.elts:
            yield n
            v = yield
            l.append(v)
        yield _tuple(l)

    @classmethod
    def list(cls, node: ast.Tuple):
        l = []
        for n in node.elts:
            yield n
            v = yield
            l.append(v)
        yield l

    @classmethod
    def set(cls, node: ast.Set):
        l = []
        for n in node.elts:
            yield n
            v = yield
            l.append(v)
        yield _set(l)

    @classmethod
    def dict(cls, node: ast.Dict):
        keys, values = [], []
        for k, v in zip(node.keys, node.values):
            yield k
            recv = yield
            keys.append(recv)
            yield v
            recv = yield
            values.append(recv)
        yield _dict((k, v) for k, v in zip(keys, values))

    @classmethod
    def nameconstant(cls, node: ast.NameConstant):
        yield node.value