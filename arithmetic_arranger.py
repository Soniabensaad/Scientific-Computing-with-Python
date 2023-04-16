#!/usr/bin/python3
def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = []
    for problem in problems:
        operands = problem.split()
        if len(operands) != 3:
            return "Error: Invalid problem format."
        operand1, operator, operand2 = operands

        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        if operator == "+":
            result = int(operand1) + int(operand2)
        else:
            result = int(operand1) - int(operand2)

        width = max(len(operand1), len(operand2)) + 2
        top_line = operand1.rjust(width)
        bottom_line = operator + operand2.rjust(width - 1)
        separator = "-" * width
        if show_answers:
            result_line = str(result).rjust(width)
            arranged_problems.append(f"{top_line}\n{bottom_line}\n{separator}\n{result_line}")
        else:
            arranged_problems.append(f"{top_line}\n{bottom_line}\n{separator}")

    return "    ".join(arranged_problems)
