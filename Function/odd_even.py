def check_odd_or_even(num):
    if(num % 2 == 0):
        print("Even number...")
    else:
        print("Odd number...")
    
input_user = int(input("Enter the number \n"))
check_odd_or_even(input_user)