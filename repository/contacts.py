from datetime import datetime, date
from typing import List
from sqlalchemy.orm import Session
from database.models import Contact
from schemas import ContactModel
from fastapi import HTTPException, status

#get contact list inside the database
async def get_contacts(skip: int, limit: int, db: Session) -> List[Contact]:
    return db.query(Contact).offset(skip).limit(limit).all()

#get a contact by 'id' inside the database
async def get_contact(contact_id: int, db: Session) -> Contact:
    return db.query(Contact).filter(Contact.id == contact_id).first()
 
#create contact inside the database
async def create_contact(body: ContactModel, db: Session) -> Contact:
    contact = Contact(first_name=body.first_name, last_name=body.last_name, email=body.email, phone=body.phone, date_birthday=body.date_birthday)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact

#update contact inside the database
async def update_contact(contact_id: int, body: ContactModel, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.email = body.email
        contact.phone = body.phone
        contact.date_birthday = body.date_birthday
        db.commit()
    return contact

#delete contact inside the database
async def remove_contact(contact_id: int, db: Session)  -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact


#get contact list by first_name, last_name or email inside the database
async def search_contacts(first_name: str, last_name: str, email: str, db: Session) -> List[Contact]:
    query = db.query(Contact)
    if first_name:
        query = query.filter(Contact.first_name == first_name)
        contacts = query.all()
    elif last_name:
        query = query.filter(Contact.last_name == last_name)
        contacts = query.all()
    elif email:
        query = query.filter(Contact.email == email)
        contacts = query.all()
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contacts not found")
    if query:
        return contacts 
    else:
        return []


#get contact list with birthdays for the next 7 days inside the database
async def get_birthday_contacts(start_date: date, end_date: date, db: Session) -> List[Contact]:
    today = datetime.today().date()
    contacts = db.query(Contact).all()
    filtered_contacts = [contact for contact in contacts if
        contact.date_birthday.replace(year=today.year) >= start_date and
        contact.date_birthday.replace(year=today.year) <= end_date]
    return filtered_contacts
   