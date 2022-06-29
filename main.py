from application import people, salary
from datetime import datetime

if __name__ == '__main__':
    print(datetime.now())
    print(people.get_employees())
    print(salary.calculate_salary())