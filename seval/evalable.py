import abc
import ast
import typing

class Evalable(abc.ABC):

    @abc.abstractmethod
    def evalable(self):
        pass

    def compile(self, s: str, *, expected: typing.Optional[ast.AST] = None):
        """compiles string into AST, if expected is passed asserts its the expected type.
        
        :param s: string to be compiled into AST.
        :type s: str
        :param expected: expected ast class type to be returned, defaults to None
        :type expected: typing.Optional[ast.AST], optional
        """

        compiled_ast = compile(
            source      = s,
            filename    = '<unknown>',
            mode        = 'eval',
            flags       = ast.PyCF_ONLY_AST,
        )

        if expected is not None:
            assert isinstance(compiled_ast, expected)
        return compiled_ast

    def allowed_nodes(self, ast_: ast.AST, *allowed: typing.List[ast.AST], **kwallowed: typing.Dict[ast.AST, typing.Callable]):
        """walks on ast_ tree and checks that all nodes are allowed.
        
        :param ast_: ast to iterate
        :type ast_: ast.AST
        """

        for n in ast.walk(ast_):
            found = False
            for a in allowed:
                if isinstance(n, a):
                    found = True
                    break

            # Checking if n was found in allowed.
            if found:
                continue

            for a, func in kwallowed.items():
                if isinstance(n, a) and func(n):
                    found = True
                    break

            # Checking if n was found in kwallowed.
            if found:
                continue

            # n isn't allowed.
            return False
        return True
