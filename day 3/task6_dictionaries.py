employees={
"aafiya":50000,
"aksha":70000,
"suzan":60000,
"yasir":80000,
"farhan":75000
}
sorted_employees = dict(
    sorted(employees.items(),key=lambda
x: x[1],reverse=True))

print("employees sorted by salary:")
for name, salary in sorted_employees.items():
    print(name, ":", salary)