from Domain.validators import PersonEventException

class PeopleRepException(PersonEventException):
    pass

class PeopleRep:
    def __init__(self):
        self.__people_list = {}
        
    def save_person(self, person):
        if self.find_person_by_id(person.personID) is not None:
            raise PeopleRepException("Id duplicat!")
        self.__people_list[person.personID] = person
    
    def find_person_by_id(self, person_id):
        try:
            return self.__people_list[person_id]
        except KeyError:
            return None
    
    def find_all(self):
        return list(self.__people_list.values())
    
    def delete_person_by_id(self, person_id):
        if self.find_person_by_id(person_id) is None:
            raise PeopleRepException("Persoana nu exista!")
        del self.__people_list[person_id]
    
    def update_person(self, person):
        if self.find_person_by_id(person.personID) is None:
            raise PeopleRepException("Persoana nu exista!")
        self.__people_list[person.personID] = person
        
    def delete_all_people(self):
        self.__people_list.clear()