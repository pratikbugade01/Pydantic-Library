from pydantic import BaseModel, EmailStr,AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated

class patient(BaseModel):
    name: str
    email:EmailStr
    age:int
    weight: float
    married: bool
    allergies: List[str]
    contact_details:Dict[str,str]
    
    
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):

        valid_domains = ['hdfc.com','icici.com']
        #abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains: 
            raise ValueError('Not a valid domain')
        
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    

def update_patient_data(patient:patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print("updated")

patient_info = {'name':'pratik','email':'abc@hdfc.com','age':19,'weight':75.3,'married':True,'allergies':['pollen','dust'],'contact_details':{'phone':'4673892765'}}

p1 = patient(**patient_info)

update_patient_data(p1)