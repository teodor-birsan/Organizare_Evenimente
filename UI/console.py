import sys
from Domain.validators import EventException, PersonException, SignException, ValidatorException
from Repository.events_repository import EventRepException
from Repository.people_repository import PeopleRepException
from Repository.sign_repository import SignPeopleRepException


class Console:
    def __init__(self, person_service, event_service, sign_service):
        self.__person_service = person_service
        self.__event_service = event_service
        self.__sign_service = sign_service
        
    def run_console(self):
        print("""
              Meniu
              1.Adauga o persoana
              2.Adauga un eveniment
              3.Sterge o persoana
              4.Sterge un eveniment
              5.Actualizeaza o persoana
              6.Acualizeaza un eveniment
              7.Afiseaza lista persoanelor
              8.Afiseaza lista evenimentelor
              9.Cauta o persoana
              10.Cauta un eveniment
              
              11.Inscrie o persoana la un eveniment
              12.Afisati evenimentele la care s-a inscris o persoana
              13.Afisati persoanele care s-au inscris la acelasi eveniment
              
              14.Afisati persoanele participante la cele mai multe evenimente
              15.Afisati primele 20(%) evenimente cu cei mai mulți participanți
              16.Lista de evenimente la care participă o persoană ordonat alfabetic după descriere, după dată
              
              c - Anuleaza o inscriere
              x - Inchide
              """)
        
    def options(self):
        while True:
            choice = input("Alegeti o operatie: ")
            match choice:
                case '1':
                    self.__add_people()                  
                case '2':
                    self.__add_events()
                case '3':
                    self.__delete_person()
                case '4':
                    self.__delete_event()
                case '5':
                    self.__update_person()
                case '6':
                    self.__update_event()
                case '7':
                    self.__print_all_people()
                case '8':
                    self.__print_all_events()
                case '9':
                    cauta = input("Cautati dupa nume sau id? nume/id ")
                    while cauta not in ['nume', 'id']:
                        print("Nu se poate face cautarea dupa parametrul introdus!")
                        cauta = input("Introduceti din nou modul de cautare: ")
                    if cauta == "nume":
                        self.__find_people_by_name()
                    elif cauta == "id":
                        self.__find_people_by_id()
                case '10':
                    cauta = input("Cautati dupa id sau descriere? id/descriere ")
                    while cauta not in ['id', 'descriere']:
                        print("Nu se poate face cautarea dupa parametrul introdus!")
                        cauta = input("Introduceti din nou modul de cautare: ")
                    if cauta == "id":
                        self.__find_event_by_id()
                    elif cauta == "descriere":
                        self.__find_event_by_description()
                case '11':
                    self.__sign_person_to_event()
                case '12':
                    self.__print_signing_list()
                case '13':
                    self.__print_event_sign_list()
                case '14':
                    self.__people_with_most_participation()
                case '15':
                    self.__print_first_20()
                case '16':
                    self.__sort_by_date_and_description()
                case 'c':
                    self.__cancel_sign()
                case 'x':
                    sys.exit()
                case _:
                    print("Operatie neimplementata!")
                    
    
    def __print_all_people(self):
        print("Lista de persoane: ")
        print(*self.__person_service.get_all_people(), sep = '\n')
        
    def __add_people(self):
            id_persoana = int(input("Id: "))
            nume_persoana = input("Nume: ")
            adresa_persoana = input("Adresa: ")
            try:
                self.__person_service.add_person(id_persoana, nume_persoana, adresa_persoana)
            except PeopleRepException as e:
                print(e)
            except ValidatorException as e:
                print(e)
            
    def __add_events(self):
            id_eveniment = int(input("Id: "))
            data_eveniment = input("Data (zz.ll): ")
            timp_eveniment = input("Timp (in zile): ")
            descriere_eveniment = input("Descriere: ")
            try:
                self.__event_service.add_event(id_eveniment, data_eveniment, timp_eveniment, descriere_eveniment)
            except EventRepException as e:
                print(e)
            except ValidatorException as e:
                print(e)
        
    def __print_all_events(self):
        print("Lista evenimentelor: ")
        print(*self.__event_service.get_all_events(), sep = '\n')
        
    def __delete_person(self):
        person_id = int(input("Introduceti id-ul persoanei pe care doriti sa o stergeti: "))
        try:
            self.__person_service.delete_person(person_id)
        except PeopleRepException as e:
            print(e)
        
    def __update_person(self):
        person_id = int(input("Introduceti id-ul persoanei pe care doriti sa o actualizati: "))
        nume = input("Introduceti noul nume: ")
        adresa = input("Introdceti noua adresa: ")
        try:
            self.__person_service.update_person(person_id, nume, adresa)
        except PeopleRepException as e:
            print(e)
    
    def __delete_event(self):
        event_id = int(input("Introduceti id-ul evenimentrului pe care doriti sa il stergeti: "))
        try:
            self.__event_service.delete_event(event_id)
        except EventRepException as e:
            print(e)
        
    def __update_event(self):
        event_id = int(input("Introduceti id-ul evenimentului pe care doriti sa il actualizati: "))
        data = input("Data (zz.ll): ")
        timp = int(input("Timp (in zile): "))
        descriere = input("Descriere: ")
        try:
            self.__event_service.update_event(event_id, data, timp, descriere)
        except EventRepException as e:
            print(e)
            
    def __sign_person_to_event(self):
        person_id = int(input("Id persona: "))
        event_id = int(input("Id eveniment: "))
        try:
            self.__sign_service.sign_person_to_event(person_id, event_id)
        except SignPeopleRepException as e:
            print(e)
            
    def __print_signing_list(self):
        person_id = int(input("Id: "))
        try:
            print(*self.__sign_service.print_person_signs(person_id), sep = '\n')
        except PersonException as e:
            print(e)
            
    def __print_event_sign_list(self):
        event_id = int(input("Id: "))
        try:
            print(*self.__sign_service.print_event_signs(event_id), sep = '\n')
        except EventException as e:
            print(e)
        
    def __people_with_most_participation(self):
        try:
            print(*self.__sign_service.people_participation(), sep = '\n')
        except SignException as e:
            print(e)
    
    def __find_people_by_name(self):
        nume = input("Nume: ")
        try:
            print(*self.__person_service.find_people_by_name(nume), sep = '\n')
        except PersonException as e:
            e = "Nu exista persoane cu acel nume!"
            print(e)
            
    def __find_people_by_id(self):
        person_id = int(input("Introduceti id-ul persoanei pe care o cautati: "))
        try:
            print(self.__person_service.check_if_exists(person_id))
        except PeopleRepException as e:
            print(e)
            
    def __find_event_by_id(self):
        event_id = int(input("Introduceti id-ul evenimentului pe care il cautati: "))
        try:
            print(self.__event_service.check_if_event_exists(event_id))
        except EventRepException as e:
            print(e)
    
    def __find_event_by_description(self):
        description = input("Descrierea: ")
        try:
            print(*self.__event_service.find_event_by_description(description), sep = '\n')
        except EventException as e:
            e = "Nu exista evenimente cu acea descriere!"
            print(e)
            
    def __print_first_20(self):
        try:
            print(*self.__sign_service.first20(), sep = '\n')
        except SignException as e:
            print(e)
            
    def __sort_by_date_and_description(self):
        person_id = int(input("Id: "))
        try:
            print(*self.__sign_service.sort_list(person_id), sep = '\n')
        except PersonException as e:
            print(e)

    def  __cancel_sign(self):
        person_id = int(input("Persoana: "))
        event_id = int(input("Evenimentul: "))
        try:
            self.__sign_service.cancel_sign(person_id, event_id)
        except SignPeopleRepException as e:
            print(e)
                   

    