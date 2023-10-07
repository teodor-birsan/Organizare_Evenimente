from Domain.validators import PersonEventException

class SignPeopleRepException(PersonEventException):
    pass

class SignPeople():
    def __init__(self, people_repository, event_repository):
        self.__people_repository = people_repository
        self.__event_repository = event_repository
        self.__sign_list = []
        
    def sign_people(self, sign):
        self.verify_existance(sign.person_id, sign.event_id)
        if self.find_sign(sign.person_id, sign.event_id) is not None:
            raise SignPeopleRepException("O persoana nu se poate inscrie de doua ori la acelasi eveniment!")
        self.__sign_list.append(sign)

    def verify_existance(self, person_id, event_id):
        if self.__people_repository.find_person_by_id(person_id) is None:
            raise SignPeopleRepException("Persoana nu exista!")
        if self.__event_repository.find_event_by_id(event_id) is None:
            raise SignPeopleRepException("Evenimentul nu exista!")
        
    def find_sign(self, person_id, event_id):
        self.verify_existance(person_id, event_id)
        for i in range(len(self.__sign_list)):
            if person_id == self.__sign_list[i].person_id and event_id == self.__sign_list[i].event_id:
                return self.__sign_list[i]
        return None
                
    def cancel_sign(self, person_id, event_id):
        self.verify_existance(person_id, event_id)
        if self.find_sign(person_id, event_id) is None:
            raise SignPeopleRepException("Persoana  nu a fost inscrisa la acest eveniment!")
        for i in range(len(self.__sign_list) -1, -1, -1):
            if person_id == self.__sign_list[i].person_id and event_id == self.__sign_list[i].event_id:
                self.__sign_list.pop(i)
    
    def show_sign_list(self):
        return self.__sign_list
    
    def delete_all_signs(self):
        self.__sign_list.clear()
    
        