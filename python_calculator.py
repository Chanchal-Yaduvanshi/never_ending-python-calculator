from python_calculator_art import logo
def add(n1,n2) :
  return n1+n2

def subtract(n1,n2) :
  return n1-n2

def multiply(n1,n2) :
  return n1*n2

def divide(n1,n2) :
  return n1/n2 

operations = {
    "+" : add,
    "-" : subtract, 
    "*" : multiply ,
    "/" : divide
}

def calculator() :
  print(logo)
  
  num1= float(input("What's the first number? "))

  for operator in operations :
    print(operator)

  isContinue = True
  while isContinue :
    operation_symbol = input("Pick an operation: ")
    num2= float(input("What's the next number? "))

    calculation_fun = operations[operation_symbol]
    answer = calculation_fun(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation:\n")
    if choice == "y" :
      num1=answer
    else :
      isContinue = False
      calculator()

calculator()
