print('Greatest among three number')
print("---------------------------")
first_number=int(input("Enter the first number: "))
second_number=int(input("Enter the second number: "))
third_number=int(input("Enter the third number: "))

if(first_number>second_number):
    if(first_number>third_number):
       print(first_number, "is greater")
    else:
        print(third_number,"is greater")
elif(second_number>third_number):
        print(second_number,"is graeter")
else:
    print(third_number,"is greater")
    