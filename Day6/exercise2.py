hi
ok


with open('exercise2.py','a') as file:

    while True:
        K = input("Please enter your input: ")
        if K == "stop":
            break 
        file.write(K + '\n')
