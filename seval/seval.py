import abc
import ast
import typing

from .evalable import Evalable

def _compile(s: str):
    """compiles string into AST.
    
    :param s: string to be compiled into AST.
    :type s: str
    """

    return compile(
        source      = s,
        filename    = '<unknown>',
        mode        = 'eval',
        flags       = ast.PyCF_ONLY_AST,
    )

def _safe_eval(ast_: ast.AST):
    """evaluate recursively.
    
    :param ast_: ast to iterate
    :type ast_: ast.AST
    """

    if not isinstance(ast_, ast.AST):
        return ast_

    key     = ast_.__class__.__name__.lower()
    func    = Evalable._NODES_HANDLERS.get(key)
    if func is None:
        raise ValueError(f'no handler for node: {key} ({ast.dump(ast_)})')
    
    gen = func(ast_)
    n = next(gen)

    while True:
        if not isinstance(n, ast.AST):
            return n

        # make it ready for send
        next(gen)

        # evaluate sub tree
        res = _safe_eval(n)

        # send result and receive new root node (or evaluation)
        n = gen.send(res)

            
def safe_eval(s: str):
    ast_ = _compile(s)
    assert isinstance(ast_, ast.Expression)
    return _safe_eval(ast_.body)