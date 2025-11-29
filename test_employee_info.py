import employee_info as e

def test_get_employees_by_age_range():
    result = []
    ans = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    ]
    result = e.get_employees_by_age_range(26,36)
    assert(result == ans)

def test_calculate_average_salary():
    result = 0
    result = e.calculate_average_salary()

    ans = 361000/6
    assert(result == ans)

def test_get_employees_by_dept():
    result = []
    result = e.get_employees_by_dept("Marketing")

    ans = [
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}
    ]

    assert(result == ans)
