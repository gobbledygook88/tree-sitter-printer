from argparse import ArgumentParser

import tree_sitter_python
from tree_sitter import Language, Parser


def format_sexpression(s, indent_level=0, indent_size=4, use_colors=True):
    """ChatGPT + TACIXAT (https://gist.github.com/TACIXAT/c5b2db4a80c812c4b4373b65e179a220)
    + Claude 3.5 Sonnet to add terminal colours"""
    output = ""
    i = 0
    # Initialize to False to avoid newline for the first token
    need_newline = False
    cdepth = []  # Track colons
    while i < len(s):
        if s[i] == "(":
            output += "\n" + " " * (indent_level * indent_size)
            output += "\033[34m(\033[0m" if use_colors else "("
            indent_level += 1
            need_newline = False  # Avoid newline after opening parenthesis
        elif s[i] == ":":
            indent_level += 1
            cdepth.append(indent_level)  # Store depth where we saw colon
            output += "\033[33m:\033[0m" if use_colors else ":"
        elif s[i] == ")":
            indent_level -= 1
            if len(cdepth) > 0 and indent_level == cdepth[-1]:
                # Unindent when we return to the depth we saw the last colon
                cdepth.pop()
                indent_level -= 1
            output += "\033[34m)\033[0m" if use_colors else ")"
            need_newline = True  # Newline needed after closing parenthesis
        elif s[i] == " ":
            output += " "
        else:
            j = i
            while j < len(s) and s[j] not in ["(", ")", " ", ":"]:
                j += 1
            # Add newline and indentation only when needed
            if need_newline:
                output += "\n" + " " * (indent_level * indent_size)
            token = s[i:j]
            output += f"\033[32m{token}\033[0m" if use_colors else token
            i = j - 1
            need_newline = True  # Next token should start on a new line
        i += 1
    return output


def main():
    argparser = ArgumentParser()
    argparser.add_argument("-f", "--file", type=str)
    argparser.add_argument(
        "--no-color", action="store_true", help="Disable syntax highlighting"
    )
    args = argparser.parse_args()
    if args.file:
        with open(args.file, "r") as f:
            code = f.read()
    else:
        print("Enter code (press Ctrl+D or Ctrl+Z on Windows when done):")
        code_lines = []
        try:
            while True:
                code_lines.append(input())
        except EOFError:
            code = "\n".join(code_lines)

    parser = Parser(Language(tree_sitter_python.language()))
    tree = parser.parse(bytes(code, "utf-8"))
    print(format_sexpression(str(tree.root_node), use_colors=not args.no_color))


if __name__ == "__main__":
    main()
