print('Hello, welcome to grade calculator!')

num1 = float(input('Enter maths grade here: '))
num2 = float(input('Enter chemistry grade here: '))
num3 = float(input('Enter physics grade here: '))

num4 = num1 + num2 + num3
average_mark = num4/3

if average_mark >= 70:
    grade = 'A'
elif average_mark >= 60:
    grade = 'B'
elif average_mark >= 50:
    grade = 'C'
elif average_mark >= 40:
    grade = 'D'
else:
    grade = 'F'

print("You're average mark was: " + str(average_mark))
print("You're overall grade was: " + grade)