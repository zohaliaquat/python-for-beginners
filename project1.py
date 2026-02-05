print("====== SCHOOL MANAGEMENT SYSTEM ======")

age = int(input("Enter student age: "))
siblings = input("Any siblings already studying? (yes/no): ").lower()

student_class = None
admission_fee = 0
monthly_fee = 0
discount = 0

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
    print("Admissions are not allowed for this age.")
    exit()

if siblings == "yes":
    discount = monthly_fee * 0.5
    print("50% sibling discount applied!")

final_monthly_fee = monthly_fee - discount

print("\n----- ADMISSION DETAILS -----")
print(f"Eligible Class        : {student_class}")
print(f"Admission Fee         : {admission_fee}")
print(f"Monthly Fee           : {monthly_fee}")
print(f"Discount              : {discount}")
print(f"Final Monthly Fee     : {final_monthly_fee}")

print("\nNOTE:")
print("Entry Test will be held on Sunday (24-12-25)")
print("You will get email from us if you clear your test")
print("Regular classes will start on Monday (15-1-26)")

print("\n---- Enter Details to Appear for Entry Test ----")

name = input("Enter your name: ")
email = input("Enter your email: ")
entry_test_fee = input("Entry Test Fee 500 submitted? (yes/no): ").lower()

selected_students = []

if email.endswith("@gmail.com") and "@" in email:
    print("Email is Valid")

    if entry_test_fee == "yes":
        print("Entry Test Fee Submitted Successfully")

        student = {
            "Name": name,
            "Email": email,
            "Class": student_class
        }

        selected_students.append(student)

        print("\nYou are successfully registered for Entry Test.")
        print("This is the information that you submitted:")
        print("Name  :", name)
        print("Email :", email)
        print("\nOur team will contact you via email.")

    else:
        print("Entry Test Fee not submitted")

else:
    print("Invalid Email")

# Admin use only
# selected_students list is visible to admin only

print("\nEntry test details are mentioned on our portal.")
print("If you have any queries, feel free to contact us.")
print("------------------- Thank You! -------------------")
