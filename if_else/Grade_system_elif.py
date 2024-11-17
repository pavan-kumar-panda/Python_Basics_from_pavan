marks = int(input("Enter the marks: "))
if(marks>=85 and marks<=100):
    print('O Grade')
elif(marks>=75 and marks<=84):
    print('A+ Grade')
elif(marks>=65 and marks<=74):
    print('A Grade')
elif(marks>=55 and marks<=64):
    print('B+ Grade')
else:
    print('Enter a correct Mark')