print("Question 5")
# Take a student’s marks and check if the marks are between 50 and 100 (inclusive).
marks=int(input("Enter Your Marks:"))
if 50<=marks<=100 :
    print("Good")
else :
    print("Work Hard")    

print("Question 6")
# Take a day name and a boolean variable is_holiday.
#  Print "Rest Day" if it is Sunday or a holiday.    
day_name=input("Enter  day name: ").lower()
if day_name=="sunday" or day_name=="saturday" :
    print("Holiday")
else:
    print("Working Day")    

print("Question:7")
# Take age and check if the person is not a minor (age is not less than 18).
age = int(input("Enter age: "))

if age >= 18:
    print("Person is NOT a minor")
else:
    print("Person is a minor")

print("Question:8 ")
# Take two boolean variables has_ticket and has_id. Allow entry only if both are True.
has_ticket=input("Yes or No:")
has_id=input("Yes or No: ")
if has_ticket=="Yes" and has_id=="Yes":
    print("Entry Allowed")
else:
    print("Entry not allowed")    