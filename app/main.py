from fastapi import FastAPI, Depends
from crud import get_all_employees, create_employee
from schema import EmployeeSchema
from database import Base, engine, sessionLocal
from sqlalchemy.orm import Session

Base.metadata.create_all(bind = engine)

app = FastAPI()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def home(db: Session = Depends(get_db)):
    context = {
        'status': 'success',
        'data' : get_all_employees(db),
    }
    return context



@app.post('/employee')
def add_employee(data : EmployeeSchema, db: Session = Depends(get_db)):
    data = create_employee(db=db, data=data)

    if isinstance(data, EmployeeSchema):

        context = {
            'status': 'success',
            'data' : data
        }
    else:
        return 'Failed'

    return context

