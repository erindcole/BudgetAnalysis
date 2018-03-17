#
# Driver for Budget Analyzer
#


def budget_calculator(income, expenses):
  return income - expenses

if __name__ == "__main__":
  income = float(input("hi, enter your moneyz:"))
  expenses = float(input("nice!, enter your splurgez:"))

  # make sure inputs are sanitized to numerics! or else... kaboom!
  # what should the type be when rep'n moneyz
  print(budget_calculator(income, expenses))
