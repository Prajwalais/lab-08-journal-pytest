def employee_details(name, emp_id, department, salary):
    result = (
        f"Employee Name: {name}\n"
        f"Employee Id: {emp_id}\n"
        f"Department: {department}\n"
        f"salary: {salary}\n"
    )
    return result


if __name__ == "__main__":
    name = "Alice"
    emp_id = "E1001"
    department = "IT"
    salary = 5500000
    print(employee_details(name, emp_id, department, salary))
    