# initializing a integer varible to store the solution
solution = 0
# list to store number and the operation
num_opr = []
while True:
    #getting a ineger value to perform operation
    num = int(input(""))
    #opr = input("Select a operation Add(+) \n Sub(-)\nDiv(/)\nMul(*)\n\nsolution(=) ")
    #getting the operation in the form of simbol
    opr = input("")
    #add
    if(opr == "+"):
        solution = solution + num
    #subtract
    elif(opr == "-"):
        solution = solution - num
    #divid
    elif(opr == "/"):
        solution = solution / num
    #product
    elif(opr == "*"):
        solution = solution * num
    #to add value to the list created
    num_opr.extend((num,opr))
    #print the list witout bracket and comma
    print(*num_opr)
    #break when user has entered "=" and display the solution
    if opr == "=":
        print(solution)
        break
