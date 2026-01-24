print("Questiom:9")
# 9. Take salary and years of experience. Approve a loan if salary 
# is greater than 50,000 and experience is more than 2 years.
salary=int(input("Enter your salary:"))
experience=int(input("Enter your experience:"))
if salary>=50000 and experience>=2:
    print("Loan Approved")
else:
    print("Disappoved")    

print("Question:10")    
# Take login_attempts and a boolean is_verified.
# Block the account if attempts are more than 3 and the user is not verified.
login_attempts = int(input("Enter login attempts: "))
is_verified = input("Yes or No: ").lower()

if login_attempts > 3 and is_verified == "no":
    print("Block")
else:
    print("Successful")

print("Questionn:11")
# Take age and citizenship status.
#  Allow voting if the age is 18 or above and the person is a citizen.
age = int(input("Enter your age: "))
citizenship = input("Are you a citizen? (Yes/No): ").lower()

if age >= 18 and citizenship == "yes":
    print("Allowed to vote")
else:
    print("Not allowed to vote")


print("Question:12")
# Take email and password. 
# Print "Login Successful" if the email is correct and the password is not empty.
email="correct@gmail.com"
password="not empty"
email=input("Enter your email")
password=input("Enter your password")
if email=="correct@gmail.com"and password=="not empty":
    print("Login Successful")
else:
    print("Login Failed")    

print("Question:13")    
#  Write a program that checks if a person is eligible to vote (age >= 18 AND citizen is True).
age = int(input("Enter your age: "))
citizenship = input("Are you a citizen? (Yes/No): ").lower()

if age >= 18 and citizenship == "yes":
    print("Allowed to vote")
else:
    print("Not allowed to vote")