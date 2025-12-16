from pydantic import BaseModel,Field
from typing import List,Dict,Optional,Annotated

class patient(BaseModel):
    
    name : Annotated[str,Field(max_length=50,title = "name of the patient",description="give the name of the patient in less than 50 chars",examples=["Pratik","kartik","om"])]
    age : Annotated[int,Field(gt = 0,strict=True)]
    weight : Annotated[float,Field(gt = 0,strict = True)]
    married : Annotated[bool,Field(default = False , description = "is the patient married or not")]
    allergies : Optional[List[str]] = Field(default=None, max_length = 5)
    contact_details : Dict[str,str] 

def insert_patient_data(patient : patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.contact_details)
    print("data inserted successfully")

def update_patient_data(patient : patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.contact_details)    
    print("data updated successfully")

patient_info ={"name":"Pratik","age":20,"weight":60,"married":"NO","contact_details":{"email":"pratikbugade555@gmail.com","phone":"9356910548"}}

patient_1 = patient(**patient_info)

insert_patient_data(patient_1)
