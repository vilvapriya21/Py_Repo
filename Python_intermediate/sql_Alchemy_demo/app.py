from database import engine, Session
from models.Employee import Employee, Base
from datetime import datetime

# Create tables (only first time)
Base.metadata.create_all(bind=engine)


def add_employee():
    session = Session()

    name = input("Enter name: ")
    salary = float(input("Enter salary: "))
    dob_str = input("Enter DOB (YYYY-MM-DD): ")

    dob = datetime.strptime(dob_str, "%Y-%m-%d").date()

    emp = Employee(name=name, salary=salary, dob=dob)

    session.add(emp)
    session.commit()
    session.close()

    print("\nEmployee added successfully!\n")


def view_employees():
    session = Session()
    employees = session.query(Employee).all()

    print("\n--- Employee List ---")
    for e in employees:
        print(e)

    session.close()


if __name__ == "__main__":
    while True:
        print("\n1. Add Employee")
        print("2. View Employees")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            break
        else:
            print("Invalid input!")
