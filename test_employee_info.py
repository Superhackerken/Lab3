import employee_info as employ

def test_get_employees_by_age_range():

    result = []
    min_age = 22
    max_age = 31
    test_arr = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]

    result = employ.get_employees_by_age_range(min_age, max_age)

    assert(result == test_arr)

def test_calculate_average_salary():

    result = 0
    test_list = [
    {"age": 30, "department": "Sales", "salary": 10000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 90000},
    {"name": "Jeff", "age": 25, "department": "Marketing", "salary": 20000}]
    test_arr = 40000

    result = employ.calculate_average_salary(test_list)

    assert(result == test_arr)

def test_get_employees_by_dept():

    result = []
    test_department = "Engineering"
    test_arr = [
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]

    result = employ.get_employees_by_dept(test_department)

    assert(result == test_arr)