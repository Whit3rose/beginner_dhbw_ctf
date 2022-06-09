import numpy as np


print("Welcome to our calculator. We can calculate your input times 4. Check it out: \n")
while True:
    calculation = np.array([0], dtype=int)
    number_input = int(input("We just have to make sure that we do not receive -4 as a value: "))

    if number_input == -4:
        print("This is not allowed!!!")
        exit()

    calculation[0] = number_input
    calculation[0] = calculation[0] * 4
    if calculation[0] == -4:
        print("flag")
    else:
        print(calculation[0])