import ast
import inspect
import typing

class Evalable(type):

    _NODES_HANDLERS = {}

    def __new__(cls, name, bases, classdict, *, evalable_nodes):
        new_handlers = []
        for node in evalable_nodes:
            if not issubclass(node, ast.AST):
                raise ValueError(f'expected ast.AST subclass got: {node}')
            key = node.__name__.lower()
            if key in Evalable._NODES_HANDLERS:
                raise ValueError(f'already got handler for {key}')
            func = classdict.get(key)
            if func is None:
                raise ValueError(f'class {cls} does not implement handler for {key}')
            if not isinstance(func, classmethod):
                raise ValueError(f'func {func} is not a classmethod of class {cls}')

            # TODO: somehow inspect sig and class method
            #if len(inspect.signature(func).parameters) != 1:
                #raise ValueError(f'func {func} signature must have only one argument')
            
            new_handlers.append(key)
        cls_ = super().__new__(cls, name, bases, classdict)
        for handler in new_handlers:
            Evalable._NODES_HANDLERS[handler] = getattr(cls_, handler)
        return cls_
            
            
