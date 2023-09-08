from datetime import date
from pydantic import BaseModel, Field, EmailStr, validator


#validation for value phone
class PhoneNumberValidator:
    @classmethod
    def validate_phone_number(cls, phone: str) -> str:
        cleaned_phone_number = ''.join(filter(str.isdigit, phone))
        if len(cleaned_phone_number) <= 13:
            return cleaned_phone_number
        else:
            raise ValueError("Phone number must contain less than or exactly 13 digits")


#validation  input data contacts
class ContactModel(BaseModel):
    first_name: str = Field(max_length=25) 
    last_name: str = Field(max_length=25)
    email: EmailStr = Field(max_length=30)
    phone: str = Field(max_length=13)
    date_birthday: date

    @validator("phone")
    def validate_phone_number_length(cls, phone):
        return PhoneNumberValidator.validate_phone_number(phone)


#validation  output data contacts
class ContactResponse(ContactModel):
    id: int

    class Config:
        orm_mode = True
        