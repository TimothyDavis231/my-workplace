#================================================================== 
# PYTHON COMPLETE PRACTICE 


from curses.ascii import isprint
from inputFunction import  project 


print("Welcome to python practice")
print("================")

# 1. variables
Name = "Timothy"
age = 20

print("\n1 variables")
print("Name:")
print("Age:")

#2 User Input
print("\n2 User Input")
username  = input("what is your name?")
print("Hello") 

#3 Number and Math
print("\n3 math operations")
a = 10
b = 5

print("addition")
print("substaction")
print("division")
print("multiplication")

#4 conditions
print("\n4 Conditions")

int(input("enter your age:"))

"if >= 18"
print("you are an adult.")
new_var =('eles')
new_var =('you are a minor')
 #5 for  Loop
print("\n5. for Loop")

for i in range(1,6): print(i)


#6 while Loop
print("\n6 while Loop") 

count =1
while count <=5:print(count)

count +=1

#7.functions
print("\n7.functions")

def greet():
    print("welcome to python!")

    greet()

    #8. Lists
    print("\n8. lists")

    language =["python, HTML, CSS"]
print("language")

#9 Dictionaries
print("\n9 dictionaries") 

student ={
    "name" "Timothy",
}
print("Student Name:" , student["name"])
print("course:", student["course"])

#10 Multiplication Table project
print("\n10 multiplication table")

number = int(input("enter a number:"))

for i in range(1,11):
    print(f"{number} x {i} {number*i}=")

    print("\n11 grade checker")

    score= float(input("enter your score"))

    if score>=80:
        print("grade A")
        elifscore =70,
        print("grade:B")
        elifscore=60,
        print("grade:C")
elifscore>=50: # type: ignore
print("Grade:D")
isprint("grade F")


print("\n12 simple calculator")

num1 = float(input("enter first number:"))
nmm2 = float(input("Enter second number:"))

print("addition= , Sum1 + sum2")
print("substraction =, num1-num2")
print("multiplication =, sum1 * num2")

if "num2"!=0:
    print("division num1/num2")

else: print("cannot divide by zero.")

print("\n13 guess the numner game")

secret_number=5
while True:
    guess= int(input("Guess the number(1-10)"))
    if guess==secret_number:
        print("congatulations! you guessed correctly.")
        break
    else:
        print("wrong guess. try again.")

        print("\n==================================")
        print("congratulations! you completed the")
        print("print practice programe.")
        print("============================")















