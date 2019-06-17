SEVAL
=====

Safe evalutaion package which allows you to evaluate expressions safely (not only literals).
[![Build Status](https://travis-ci.org/DanielSolomon/seval.svg?branch=master)](https://travis-ci.org/DanielSolomon/seval)

Usage
-----
```
>>> import ast
>>> import seval
>>> safe_expression = '2 ** 3'
>>> ast.literal_eval(safe_expression)
ValueError: malformed node or string
>>> seval.safe_eval(safe_expression)
8
>>> seval.safe_eval('pow(2, 3)')
ValueError: cannot evaluate pow(2,3) safely
```