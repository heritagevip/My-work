school_name = "FUTES"
school_address = "IYIN EKITI"
course_studing = "Software Engineering"
student_name = "HERITAGE"
students = ["heritage", "john", "michael", "susan"]
student_age = "6 7"
total_fees = (150000)
amount_paid = (10000)
has_scolarship = (False)
student_remark = (" is a good boy")
balance = total_fees - amount_paid
for name in students:
  if balance == 0:
    print(f"status you are cleared for the semester {name} {student_remark}")
  elif balance <= 50000:
     print(f"{name} im giving you last warning before i wound you ")
  else:
    print(f"{name} go to your father house ")