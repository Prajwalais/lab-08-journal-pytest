from employee import employee_details

def test_employee_details():
    expected_output = (
        "Employee Name: Alice\n"
        "Employee Id: E1001\n"
        "Department: IT\n"
        "salary: 5500000\n"
    )

    assert employee_details("Alice", "E1001", "IT", 5500000) == expected_output
