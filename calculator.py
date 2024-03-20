import os
from art import logo


def add(a, b):
  return a + b

def sub(a, b):
  return a - b

def mul(a, b):
  return a * b

def div(a, b):
  return a / b

operations = {
  "+" : add,
  "-" : sub,
  "*" : mul,
  "/" : div
}

def calculator():
  print(logo)
  num1 = float(input("Enter first number: "))

  for operators in operations:
    print(operators)

  should_continue = True
  while should_continue:
    choose_operator = input("Pick an operations: ")
    num2 = float(input("Enter next number: "))
    calculation_operator = operations[choose_operator]
    result = calculation_operator(num1, num2)

    print(f"\n\nResult of {num1} {choose_operator} {num2} is {result}\n")

    if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower() == 'y':
      num1 = result
    else:
      should_continue = False
      calculator()


calculator()


