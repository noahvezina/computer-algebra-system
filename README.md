# Computer Algebra System in Python

## Description

This computer algebra system will be a command line REPL that allows for basic symbolic manipulation.


Implementation objectives:
- Simplification
- Certain elementary functions
- Differentiation

## Syntax

Each of line of input must either be an expression or a declaration.
Expressions are evaluated immediately whereas declared objects can be called later on.
Later, support might be added for equation declaration and manipulation.

### Declarations

A declaration assigns a name to an expression for later use. Declarations begin with the 'let' keyword, followed by a name, the ':=' assignment operator and an expression (see below). Declaration names can include letters, numbers, or underscores but they must begin with a letter.

```
>>> let quadratic := 3x^2 + 9x - 3
```

```
>>> let test_construction := 1 + cos(1/(x)) + sin(1/(x^2)) 
```

### Expressions

An expression is a grouping of one or more terms. An expression can be part of a declaration (as mentioned above), or called on their own. When called, expressions are evaluated and simplified (see below).

```
>>> diff(quadratic, x)
6x + 9
```
```
>>> 9x + 0 + 3 + 5 + 2
9x + 10
```