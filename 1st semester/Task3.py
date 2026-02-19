while True:
    a = int(input("Please enter the number 'left': "))
    b = int(input("Please enter the number 'right': "))
    if b < a:
        print("Please make sure that your range is correct!")
        continue

    elif a == b:
        print(a)

        
    else:
        for i in range(a + 1, b + 1):
            a = a & i

        print(f"Your result is {a}")
        
    choice = int(input("There you go! If you'd like to continue, press 1. If not, press 0: "))

    if choice == 1:
        print("Okay, there we go!")
        continue
    
    elif choice == 0:
        print("Thank you, see u))")
        break
