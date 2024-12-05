
# A SIMPLE CALCULATOR PROJECT


def addition(n1,n2):
    return n1+n2

def subtraction(n1,n2):
    return n1-n2

def multiplication(n1,n2):
    return n1*n2

def division(n1,n2):
    return n1/n2

operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}
def calculator():
    should_accumulate = True
    n1 = float(input("Enter first number \n"))

    while should_accumulate:
        for symbols in operations:
            print(symbols)
        symbol=input("Pick an operation: \n")    
        n2 = float(input("Enter second number \n"))    
        answer = operations[symbol](n1,n2)
        print(f"{n1} {symbol} {n2} = {answer}")

        choice = input("Type Yes if you want to continue the operations with your answer \n")
        if choice == "Yes":
            n1=answer
        else:
            should_accumulate = False 
            calculator()
            
calculator()               
    
