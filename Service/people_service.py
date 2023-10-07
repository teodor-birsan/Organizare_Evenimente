from Domain.entities import Person

class PeopleService:
    def __init__(self, person_repository, person_exception, person_validator):
        self.__person_repository = person_repository
        self.__person_validator = person_validator
        self.__person_exception = person_exception

    def get_all_people(self):
        return self.__person_repository.find_all()
    
    def add_person(self, person_id, name, adress):
        person = Person(person_id, name, adress)
        self.__person_validator.validate(person)
        self.__person_repository.save_person(person)
        return self.get_all_people()
        
    def delete_person(self, personID):
        self.__person_repository.delete_person_by_id(personID)
        return self.get_all_people()
        
    def update_person(self, person_id, name, adress):
        person = Person(person_id, name, adress)
        self.__person_repository.update_person(person)
        return self.get_all_people()
        
    def check_if_exists(self, person_id):
        """Functia primeste ca parametru id-ul unei persoane si o cauta in dictionar. Daca o gaseste va returna obiectul din dictionar cu cheia "person_id".
        Daca nu, ea returneaza 'None'.

        Args:
            person_id (str): id-ul persoane pt care se verifca existenta in dictionar

        Returns:
            object: returneaza obiectul Person(), daca exista. Altfel returneaza None
        """
        return self.__person_repository.find_person_by_id(person_id)
    
    def find_people_by_name(self, name):
        """Functia primeste ca parametru un nume si returneaza o lista cu toate persoanele care au numele respectiv. Daca nu exista persoane cu acel nume,
        functia retuneaza None.

        Args:
            name (str): numele persoanelor pe care le cauta functia

        Returns:
            list: lista cu persoane care au numele dat
        """
        pplist = self.__person_repository.find_all()
        name_list = []
        for i in range(len(pplist)):
            if pplist[i].name == name:
                name_list.append(pplist[i])
        if len(name_list) == 0:
            raise self.__person_exception("Nu s-au gasit persoane cu numele dat!")
        return name_list