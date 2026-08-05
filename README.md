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

A declaration assigns a name to an expression for later use. Declarations begin with the 'let' keyword, followed by a name, the ':=' assignment operator and an expression (see below). Declaration names can include one or more letters, numbers, or underscores; they must begin with a letter. 

```
>>> let quadratic := 3x^2 + 9x - 3
```

```
>>> let test_construction := 1 + cos(1/(x)) + sin(1/(x^2)) 
```

### Functions

Functions are called as an indentifier followed by arguments within parentheses. There is a set list of predefined functions available for use. 

```
>>> diff(my_expr, u)
>>> cos(sin(x))
>>> sqrt(b^2 - 4ac)
```

### Variables

As opposed to declared expressions, variables are single-letter indentifiers used to represent arbitrary values. They do not carry additional meaning. If an identifier is not a previously declared expression or function call, it is broken up into single-letter variables.

```
>>> xsin(x) + 9quadratic
```

In the above example, "xsin(x)" will parse as a variable "x" multiplied by the function call "sin(x)". Similarly, "9quadratic" will parse as 9 multiplied by the saved expression "quadratic"

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

## Attributions

The lexer, parser, and much of the interpreter as a whole was written following Robert Nystrom's [Crafting Interpreters](https://craftinginterpreters.com/contents.html).