print("====== SCHOOL MANAGEMENT SYSTEM ======")

age = int(input("Enter student age: "))
siblings = input("Any siblings already studying? (yes/no): ").lower()

# Initialize variables
student_class = None
admission_fee = 0
monthly_fee = 0
discount = 0

# Admission rules
if 3 <= age <= 5:
    student_class = 1
    admission_fee = 15000
    monthly_fee = 4000

elif 6 <= age <= 8:
    student_class = 2
    admission_fee = 18000
    monthly_fee = 5000

elif 9 <= age <= 10:
    student_class = 3
    admission_fee = 20000
    monthly_fee = 6000

elif 11 <= age <= 12:
    student_class = 4
    admission_fee = 22000
    monthly_fee = 7000

elif 13 <= age <= 14:
    student_class = 5
    admission_fee = 24000
    monthly_fee = 8000

elif 15 <= age <= 16:
    student_class = 6
    admission_fee = 26000
    monthly_fee = 9000

else:
    print(" Admissions are not allowed for this age.")
    exit()

# Discount logic
if siblings == "yes":
    discount = monthly_fee * 0.5
    print("50% sibling discount applied!")

final_monthly_fee = monthly_fee - discount

# Final output
print("\n----- ADMISSION DETAILS -----")
print(f"Eligible Class        : {student_class}")
print(f"Admission Fee         : {admission_fee}")
print(f"Monthly Fee           : {monthly_fee}")
print(f"Discount              : {discount}")
print(f"Final Monthly Fee     : {final_monthly_fee}")
print("Note:\n Entry Test will be held on Sunday (24-12-25)")
print("You will get email from us if you clear your Test")
print("Regular classes will start on Monday (15-1-26)")

email=input("Enter your email: ")
if email.endswith("@gmail.com") and email.index("@") >0 :
    print("Valid Email")
else:
    print("Invalid Email")    

print("Thank You")    