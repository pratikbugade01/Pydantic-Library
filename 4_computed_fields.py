from pydantic import BaseModel, EmailStr,computed_field
from typing import List,Dict

class patient(BaseModel):
    name: str
    email:EmailStr
    age:int
    weight: float #kg
    height: float #mtr
    married: bool
    allergies: List[str]
    contact_details:Dict[str,str]
    

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi

    
def update_patient_data(patient:patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print("bmi : ",patient.bmi)
    print("updated")

patient_info = {'name':'pratik','email':'abc@hdfc.com','age':65,'weight':75.3,'height':1.72,'married':True,'allergies':['pollen','dust'],'contact_details':{'phone':'4673892765','emergency':'8598756321'}}

p1 = patient(**patient_info)

update_patient_data(p1)