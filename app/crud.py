from sqlalchemy.orm import Session
from models import Employee
from schema import EmployeeSchema
from sqlalchemy.exc import IntegrityError


def get_all_employees(db: Session):
    return db.query(Employee).all()


def create_employee(db:Session, data:EmployeeSchema):
    """
    Insert Data:
        Create a New Employee Entery into the Database
    """
    try:
        employee_data = Employee(name = data.name, phone = data.phone)
        db.add(employee_data)
        db.commit()
        db.refresh(employee_data)

    except IntegrityError: 
        return 'Record Already Exists in Database with same given data '
    return employee_data


def employee_details(db: Session, emp_id:int):
    '''
    Return the Specific Employees Data Stored in the Database.\n
    Fetch Employee Data using Employee id
    '''
    employee_data = db.query(Employee).filter(Employee.id == emp_id).first()
    return employee_data


def employee_update(db:Session, emp_id:int, data:EmployeeSchema):
    employee_data = db.query(Employee).filter(Employee.id == emp_id).first()
    if employee_data:
        employee_data.name = data.name
        employee_data.phone = data.phone
    
        db.commit()
        db.refresh(employee_data)

    return employee_data


def delete_employee(db:Session, emp_id : int):
    emp_data = db.query(Employee).filter(Employee.id == emp_id).first()
    db.delete(emp_data)
    db.commit()

    return emp_data



