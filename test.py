school_name = "FUTES"
school_address = "IYIN EKITI"
course_studing = "Software Engineering"
student_name = "HERITAGE"
student_age = "6 7"
total_fees = (150000)
amount_paid = (110000)
has_scolarship = (False)
student_remark = ("Heritage is a good boy")
balance = total_fees - amount_paid
if balance == 0: 
  print("Status Cleared")
elif balance<50000:
  print("status; Pay us as soon as possible")
else: 
  print("Status; Denied")