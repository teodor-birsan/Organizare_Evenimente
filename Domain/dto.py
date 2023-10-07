from dataclasses import dataclass

@dataclass
class PeopleDTO:
    person_name: str
    number_of_events: int
    
    def __str__(self):
        return f"{self.person_name} participa la {self.number_of_events} eveniment(e)."
    
    
@dataclass
class EventsDTO:
    event_description: str
    number_of_participants: int
    
    def __str__(self):
        return f"La evenimentul {self.event_description} participa {self.number_of_participants} persoane."
    
    
@dataclass
class EventSortDTO:
    event_day: str
    event_month: str
    event_descr: str
    
    def __str__(self):
        return f"Evenimentul {self.event_descr} are loc la data de {self.event_day}/{self.event_month}."
    
    
class EventSortDTOAssembler:
    @staticmethod
    def create_event_sort_dto(event):
        date = event.date.split(".")
        event_day = date[0]
        event_month = date[1]
        event_descr = event.description
        return EventSortDTO(event_day, event_month, event_descr)
            
class PeopleDTOAssembler:
    @staticmethod
    def create_person_dto(person, sign_list):
        number_of_events = len(sign_list)
        person_name = person.name
        return PeopleDTO(person_name, number_of_events)
    
    
    
class EventDTOAssembler:
    @staticmethod
    def create_event_dto(event, sign_list):
        event_description = event.description
        number_of_participants = len(sign_list)
    
        return EventsDTO(event_description, number_of_participants)    
    

