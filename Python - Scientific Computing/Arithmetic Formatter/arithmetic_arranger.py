def arithmetic_arranger(problems, show_answers=True):
    if len(problems) > 5:
        return "Error: Too many problems."

    top_line = ""
    bottom_line = ""
    line = ""
    result_line = ""

    for problem in problems:
        # separate the operands
        operand1, operator, operand2 = problem.split()

        try:
            # Operands must contain only digits
            if not operand1.isdigit() and not operand2.isdigit():
                return "Error: Numbers must only contain digits."

            # Operands max length is 4 digits
            if len(operand1) > 4 or len(operand2) > 4:
                return "Error: Numbers cannot be more than four digits."

            # Convert operand to integer
            num1 = int(operand1)
            num2 = int(operand2)

            # Operation Calculation
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            else:
                return "Error: Operator must be '+' or '-'."

            # Adjust column width
            width = max(len(operand1), len(operand2)) + 2

            # Add operations to designated lines
            top_line += operand1.rjust(width) + "    "
            bottom_line += operator + operand2.rjust(width - 1) + "    "
            line += "-" * width + "    "
            result_line += str(result).rjust(width) + "    "
        except ValueError as e:
            return str(e)

    arranged_problems = top_line.rstrip() + "\n" + bottom_line.rstrip() + "\n" + line.rstrip() + "\n" + result_line.rstrip()

    return arranged_problems

"""
Function Call Example:
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problems))
"""
