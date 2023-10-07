from dataclasses import dataclass

@dataclass
class Person:
    personID: int
    name: str
    adress: str
    
    # Print Person
    
    def __str__(self):
        return f"ID: {self.personID}, Nume: {self.name}, Adresa: {self.adress} \n"
@dataclass
class Event:
    ID: int
    date: str
    time: int
    description: str
        
    # Print Event
    
    def __str__(self):
        return f"ID: {self.ID}, Data (zz/ll): {self.date}, Timp (in zile): {self.time}, Descriere: {self.description} \n"
    
    
@dataclass
class Sign:
    person_id: int
    event_id: int
    
