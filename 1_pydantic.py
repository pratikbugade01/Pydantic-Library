from pydantic import BaseModel
from typing import List,Dict,Optional

class patient(BaseModel):
    
    name : str
    age : int
    weight : float
    married : bool = False
    allergies : Optional[List[str]] = None 
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

patient_info ={"name":"Pratik","age":"20","weight":"60","married":"NO","contact_details":{"email":"pratikbugade555@gmail.com","phone":"9356910548"}}

patient_1 = patient(**patient_info)

insert_patient_data(patient_1)
