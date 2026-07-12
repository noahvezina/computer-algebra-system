# Computer Algebra System in Python

## Description

This computer algebra system will be a command line REPL that allows for basic symbolic manipulation, including:

- Differentiation
- Integration
- Equation solving
- Expression simplification

## Syntax

Each of line of input must either be an expression or a declaration.
Expressions are evaluated immediately whereas declared objects can be called later on.
Declarations are written using the 'let' keyword, the ':=' operator, and explicit typing.

### A function declaration

Functions use the 'fn' type hint and can be defined with one or more arguments.

```
> let fn f(x) := x^2 + x - 1
```

### An equation declaration

Equations use the 'eq' type hint.

```
> let eq example := a/b - c/d = 3a + 2b + c - d
```

### An expression declaration

Expressions use the 'expr' type hint.

```
> let expr trig1 := sin(7*PI*x/4)
```

### Examples

```
> diff(3x^2 + 2x - 1)
6x + 2
```
```
> let fn population(t) = 100*EULER^(0.8t)
> diff(population(t), t)
80*EULER^(0.8t)
```