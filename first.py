school_fees = 150000
student_data = {
    "heritage is late ": 100000,
    "john is not late": 15000,
    "victor is late": 70000,
    "daniel is not late": 90000,
    "soj is late":120000,
}
for name, paid in student_data.items():
    balance = school_fees - paid 
if "late" in name:
    print(f"{name}{balance + 5000}")
else:
    print(f"{name} cleared")