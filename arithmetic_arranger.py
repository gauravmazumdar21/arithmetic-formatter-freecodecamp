def arithmetic_arranger(problems, show_answers=False):
  # Check the number of problems
  if len(problems) > 5:
      return "Error: Too many problems."

  first_operand = []
  second_operand = []
  operators = []

  for problem in problems:
      pieces = problem.split()
      first_operand.append(pieces[0])
      operators.append(pieces[1])
      second_operand.append(pieces[2])

  # Check for * or /
  if "*" in operators or "/" in operators:
      return "Error: Operator must be '+' or '-'."

  # Check the digits
  for i in range(len(first_operand)):
      if not (first_operand[i].isdigit() and second_operand[i].isdigit()):
          return "Error: Numbers must only contain digits."

  # Check the length
  for i in range(len(first_operand)):
      if len(first_operand[i]) > 4 or len(second_operand[i]) > 4:
          return "Error: Numbers cannot be more than four digits."

  first_line = []
  second_line = []
  third_line = []
  fourth_line = []

  for i in range(len(first_operand)):
      if len(first_operand[i]) > len(second_operand[i]):
          first_line.append(" " * 2 + first_operand[i])
      else:
          first_line.append(" " * (len(second_operand[i]) - len(first_operand[i]) + 2) + first_operand[i])

  for i in range(len(second_operand)):
      if len(second_operand[i]) > len(first_operand[i]):
          second_line.append(operators[i] + " " + second_operand[i])
      else:
          second_line.append(operators[i] + " " * (len(first_operand[i]) - len(second_operand[i]) + 1) + second_operand[i])

  for i in range(len(first_operand)):
      third_line.append("-" * (max(len(first_operand[i]), len(second_operand[i])) + 2))

  if show_answers:
      for i in range(len(first_operand)):
          if operators[i] == "+":
              ans = str(int(first_operand[i]) + int(second_operand[i]))
          else:
              ans = str(int(first_operand[i]) - int(second_operand[i]))

          if len(ans) > max(len(first_operand[i]), len(second_operand[i])):
              fourth_line.append(" " + ans)
          else:
              fourth_line.append(" " * (max(len(first_operand[i]), len(second_operand[i])) - len(ans) + 2) + ans)

      arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line) + "\n" + "    ".join(fourth_line)
  else:
      arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line)

  return arranged_problems
