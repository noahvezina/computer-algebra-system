# Computer Algebra System in Python

## Description

This computer algebra system is a command line REPL that allows for reallly basic symbolic manipulation of polynomials. The implementation includes a recursive descent parser, expression simplification, and differentiation.

## Syntax

Each of line of input must either be an expression or a declaration.
Expressions are evaluated immediately whereas declared expressions can be called later on.

### Declarations

A declaration assigns a name to an expression for later use. Declarations begin with the 'let' keyword, followed by a name, the ':=' assignment operator, and the to-be-assigned expression. Declaration names must begin with a letter and can include letters, numbers, or underscores.

```
>>> let quadratic := 3x^2 + 9x - 3
```

```
>>> let test_construction := 1 + cos(1/(x)) + sin(1/(x^2)) 
```

### Functions

Functions are called as an indentifier followed by zero or more arguments within parentheses. There is a set list of predefined functions available for use. 

```
>>> diff(my_expr, u)
```

### Variables

As opposed to declared expressions, variables are single-letter indentifiers used to represent arbitrary values. They do not carry inherent meaning. If an identifier is not a previously declared expression or function call, it is broken up into single-letter variables.

```
>>> xdiff(x) + 9quadratic
```

In the above example, "xsin(x)" will parse as a variable "x" multiplied by the function call "sin(x)". Similarly, "9quadratic" will parse as 9 multiplied by the saved expression "quadratic"

### Expressions

An expression is a grouping of one or more terms. An expression can be part of a declaration, or called on their own. When called on their own, expressions are evaluated and automatically simplified.

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