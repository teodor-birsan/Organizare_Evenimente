from Repository.people_repository import PeopleRep, PeopleRepException
from Domain.entities import Event, Person
from Repository.events_repository import EventRep, EventRepException

class PeopleTextFile(PeopleRep):
    def __init__(self, file_name, person_validator):
        super().__init__()
        self.__file_name = file_name
        self.__person_validator = person_validator
        self.load_data()
    
    def load_data(self):
        with open(self.__file_name) as f:
            for line in f:
                person_string = line.split(",")
                person = Person(int(person_string[0]), person_string[1], person_string[2])
                self.__person_validator.validate(person)
                super().save_person(person)
                
    def save_person(self, person):
        with open(self.__file_name, "a") as f:
            super().save_person(person)
            f.write('\n' + str(person.personID) + "," + person.name + "," + person.adress)
            
    def update_person(self, person):
        if super().find_person_by_id(person.personID) is None:
            raise PeopleRepException("Persoana nu exista!")
        super().update_person(person)
        with open(self.__file_name, "r+") as f:
            d = f.readlines()
            f.seek(0)
            for line in d:
                if line.startswith(str(person.personID)):
                    f.write(str(person.personID) + "," + person.name + "," + person.adress + '\n')
                else:
                    f.write(line)
            f.truncate()
                         
    def delete_person_by_id(self, id):
        if super().find_person_by_id(id) is None:
            raise PeopleRepException("Persoana nu exista!")
        super().delete_person_by_id(id)
        with open(self.__file_name, "r+") as f:
            d = f.readlines()
            f.seek(0)
            for line in d:
                if not line.startswith(str(id)):
                    f.write(line)
            f.truncate()
                    
class EventTextFile(EventRep):
    def __init__(self, file_name, event_validator):
        super().__init__()
        self.__file_name = file_name
        self.__event_validator = event_validator
        self.load_data()
        
    def load_data(self):
        with open(self.__file_name) as f:
            for line in f:
                event_string = line.split(",")
                event = Event(int(event_string[0]), event_string[1], int(event_string[2]), event_string[3])
                self.__event_validator.validate(event)
                super().save_event(event)
                
    def save_event(self, event):
        with open(self.__file_name, "a") as f:
            super().save_event(event)
            f.write('\n' + str(event.ID) + "," + event.date + "," + str(event.time) + "," +  event.description)
            
    def update_event(self, event):
        if super().find_event_by_id(event.ID) is None:
            raise EventRepException("Evenimentul nu exista!")
        super().update_event(event)
        with open(self.__file_name, "r+") as f:
            d = f.readlines()
            f.seek(0)
            for line in d:
                if line.startswith(str(event.ID)):
                    f.write(str(event.ID) + "," + event.date + "," + str(event.time) + "," +  event.description + '\n')
                else:
                    f.write(line)
            f.truncate()
            
    def delete_event_by_id(self, id):
        if super().find_event_by_id(id) is None:
            raise EventRepException("Evenimentul nu exista!")
        super().delete_event_by_id(id)
        with open(self.__file_name, "r+") as f:
            d = f.readlines()
            f.seek(0)
            for line in d:
               if not line.startswith(str(id)):
                    f.write(line)
            f.truncate() 

    