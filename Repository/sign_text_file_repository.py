from Repository.sign_repository import SignPeople, SignPeopleRepException
from Domain.entities import Sign

class SignTextFile(SignPeople):
    def __init__(self, file_name, people_repository, events_repository):
        self.__people_repository = people_repository
        self.__events_repository = events_repository
        super().__init__(self.__people_repository, self.__events_repository)
        self.__file_name = file_name
        self.__load_data()
        
    def __load_data(self):
        with open(self.__file_name) as f:
            for line in f:
                sign_array = line.split(",")
                sign = Sign(int(sign_array[0]), int(sign_array[1]))
                super().sign_people(sign)
                
    def sign_people(self, sign):
        with open(self.__file_name, "a") as f:
            super().sign_people(sign)
            f.write('\n' + str(sign.person_id) + "," + str(sign.event_id))
            
    def cancel_sign(self, person_id, event_id):
        if super().find_sign(person_id, event_id) is None:
             raise SignPeopleRepException("Persoana nu a fost inscrisa la acest eveniment!")
        super().cancel_sign(person_id, event_id)
        with open(self.__file_name, "r+") as f:
            d = f.readlines()
            f.seek(0)
            for line in d:
                if line != f"{person_id},{event_id}\n":
                    f.write(line)
            f.truncate()
        