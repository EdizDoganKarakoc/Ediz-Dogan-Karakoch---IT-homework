alph = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

column = []
for i in alph:
    column.append(i)

for i in alph:
    for j in alph:
        element = i + j
        column.append(element)




while True:
    choice = int(input("What's the number of the column that you would like to learn the 'Excel name' for? (press 0 to exit the loop<3): "))
    
    if choice == 0:
        break

    answer = column[choice - 1]
    print(f"The name of your column is {answer} !")


print("Thank you, see you later!")
