# Tree-sitter Printer

A command-line tool that prints the Abstract Syntax Tree (AST) of Python code in a readable S-expression format with syntax highlighting.

## Features

- Pretty-prints Python ASTs with proper indentation
- Syntax highlighting for better readability
- Accepts input from files or stdin
- Option to disable colors

## Installation

Install using pipx:

```bash
pipx install git+https://github.com/gobbledygook88/tree-sitter-printer.git
```

or via [uvx](https://docs.astral.sh/uv/guides/tools/#running-tools):

```bash
uvx --from git+https://github.com/gobbledygook88/tree-sitter-printer.git tree-sitter-printer
```

To avoid typing the full URL every time, you can [install it with uv](https://docs.astral.sh/uv/guides/tools/#installing-tools):

```bash
uv tool install git+https://github.com/gobbledygook88/tree-sitter-printer.git
```

## Usage

Print the tree-sitter tree of a file:

```bash
tree-sitter-printer -f my_script.py
```

Print the tree-sitter tree of code from stdin:

```bash
echo "print('Hello, world!')" | tree-sitter-printer
```

```lisp
(module
    (expression_statement
        (call
            function:
                (identifier)
            arguments:
                (argument_list
                    (string
                        (string_start)
                        (string_content)
                        (string_end))))))
```

Disable syntax highlighting:

```bash
echo "print('Hello, world!')" | tree-sitter-printer --no-color
```
