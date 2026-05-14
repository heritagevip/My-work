school_name = "FUTES"
school_address = "IYIN EKITI"
course_studing = "Software Engineering"
student_name = "HERITAGE"
students = ["heritage", "john", "michael", "susan"]
student_age = ["17", "18", "19", "20"]
total_fees = (150000)
amount_paid = (10000)
has_scolarship = (False)
student_remark = (" is a good boy")
balance = total_fees - amount_paid
student_data = {
  "heritage": 150000,
  "john": 0,
  "micheal": 90000,
  "susan": 120000,
}
for name, paid in student_data.items():
  balance = total_fees - paid
  print(f"{name} paid {paid} and your balance is {balance}")