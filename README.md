SEVAL
=====

Safe evalutaion package which allows you to evaluate expressions safely (not only literals).
[![Build Status](https://travis-ci.org/DanielSolomon/seval.svg?branch=master)](https://travis-ci.org/DanielSolomon/seval)

What's safe?
------------

Currently `seval` evaluates:

* arithmetic expressions
* literals
* any combination of the above

Usage
-----
```
>>> import ast
>>> import seval
>>>
>>> # Safe expression!
>>> safe_expression = '2 ** 3'
>>> ast.literal_eval(safe_expression)
ValueError: malformed node or string
>>> seval.safe_eval(safe_expression)
8
>>>
>>> # Function call - unsafe!
>>> seval.safe_eval('pow(2, 3)')
ValueError: no handler for node: call (Call(func=Name(id='pow', ctx=Load()), args=[Num(n=2), Num(n=3)], keywords=[]))
>>>
>>> # Another safe expression (which is combination of literals and arithmetic operations)!
>>> another_safe_expression = '["a", 5 * 5]'
>>> ast.literal_eval(another_safe_expression)
ValueError: malformed node or string
>>> seval.safe_eval(another_safe_expression)
['a', 25]
```