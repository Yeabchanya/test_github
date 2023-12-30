
print("--------------------------------------\n")
print("-----        CALCULATOR          -----\n")
print("--------------------------------------\n")
n1 = int(input("Enter Num1: "))
Operator = input("operator: ")
n2 = int(input("Enter Num2: "))

if (Operator == "+"):
    result = n1 + n2
    print("Num + Num= "+str(result))
elif (Operator == "-"):
    result = n1 - n2
    print("Num - Num= " + str(result))
elif (Operator == "*"):
    result = n1 * n2
    print("Num * Num= " + str(result))
elif (Operator == "/"):
    result = n1 / n2
    print("Num / Num= " + str(result))
else: print("operator is invalde")
