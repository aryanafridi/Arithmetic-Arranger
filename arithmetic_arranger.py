equations_list = ['3801 - 2', '123 + 49']
list1 = ["1234 + 1", "2222-22"]


def arithmetic_arranger(equation_list, answers=False):
    output = ['', '', '']
    if len(equation_list) > 5:
        return "Error: Too many problems."
    else:
        for i in equation_list:
            space = 0 if len(equation_list)-1 == equation_list.index(i) else 4
            i = i.replace(" ", "")
            if i.__contains__("/") or i.__contains__("*"):
                return "Error: Operator must be '+' or '-'."
            else:
                operator = "+" if i.__contains__("+") else "-"
                numbers = i.split(operator)
                length = len(numbers[0]) if len(numbers[0]) > len(numbers[1]) else len(numbers[1])
            for number in numbers:
                if not number.isdigit():
                    return "Error: Numbers must only contain digits."
                elif len(number) > 4:
                    return "Error: Numbers cannot be more than four digits."
                else:
                    if not numbers.index(number):
                        output[0] += "{:>{}}{:^{}}".format(numbers[0], length + 2, "", space)
                    else:
                        output[1] += "{:<2}{:>{}}{:^{}}".format(operator, numbers[1], length, "", space)
            else:
                output[2] += "{:->{}}{:^{}}".format("", length + 2, "", space)
                if answers:
                    num_1 = int(numbers[0])
                    num_2 = int(numbers[1])
                    answer = num_1 + num_2 if operator == "+" else num_1 - num_2
                    output.append("") if len(output) == 3 else 0
                    output[3] += "{:>{}}{:^{}}".format(answer, length + 2, "", space)
    return "\n".join(output)


print(arithmetic_arranger(equations_list, True))
