from typing import List, Dict, Annotated, Optional
from pydantic import Field, BaseModel


class EmployeeSchema(BaseModel):
    name : Annotated[str, Field(...,description='Name of the Employe', max_length=60, min_length=10)]
    phone : Annotated[int, Field(..., description="Phone number of the employee")]