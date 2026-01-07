from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class patient(BaseModel):

    name: str
    gender: str
    age: int
    address : Address


address_dict = {'city':'maligre','state':'maharashtra','pin':'416505'}

Address1 = Address(**address_dict)

patient_dect ={'name':'pratik','gender':'male','age':'20','address':Address1}

patient1 = patient(**patient_dect)

print(patient1)
print(patient1.address.pin)