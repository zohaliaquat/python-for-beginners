print(" Quesion 1")
# Take a person’s age and check if they are eligible for
#  a discount if the age is less than 18 or greater than 60.

Age=int(input("Enter your Age: "))
if Age<18 or Age>60 :
    print("Eligible for Discount")
else:
    print("Not Eligible For Discount")    

print("Question 2")
 # Take age and a boolean variable is_student. Print "Eligible for scholarship"
 # if the age is under 25 and the person is a student.

age=int(input("Enter your age:"))
is_student=input("You are student True or False: ")
if age<=25 or is_student==True:
    print("Eligible for scholarship")
else:
    print("Not Eligible")


print("Question 3")
# Take username and password. Grant access if the username is "admin" and the password is "1234"
username=input("Enter your username:")
password=input("Enter your password: ")
if  username == "admin" and  password == "1234":
    print("Login")
else :
    print("Worng informations added")    

print("Question:4")
# Take temperature as input and print "Extreme Weather" if the temperature is below 0 or above 40.
temperature=int(input("Enter temperature:"))
if temperature<=0 or temperature>=40:
    print("Extreme Weather")
else:
    print("Normal Weather")        
    