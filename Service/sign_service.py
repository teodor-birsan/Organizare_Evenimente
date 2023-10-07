from Domain.dto import EventDTOAssembler, EventSortDTOAssembler, PeopleDTOAssembler
from Domain.entities import Sign

class SignSerivce():
    def __init__(self, sign_repository, people_repository, event_repository, person_exception, event_exception):
        self.__sign_repository = sign_repository
        self.__people_repository = people_repository
        self.__event_repository = event_repository
        self.__person_exception = person_exception
        self.__event_exception = event_exception
        
    def sign_person_to_event(self, person_id, event_id):
        """Inscrie o persoana la un eveniment.

        Args:
            person_id (int): id-ul persoanei
            event_id (int): id-ul evenimentului
        """
        sign = Sign(person_id, event_id)
        self.__sign_repository.sign_people(sign)
        
    def print_person_signs(self, person_id):
        """Functia are ca parametru id-ul unei persoane. Se verifica daca persoana se afla in lista cu persoane; daca exista, se cauta in lista cu inscrieri
        toate evenimentele la care participa persoana data. Functia returneaza o lista cu toate evenimentele la care participa persoana respectiva.

        Args:
            person_id (int): id-ul persoanei 

        Raises:
            self.__person_exception: eroarea aruncata daca persoana nu exista

        Returns:
            list: o lista cu toate evenimentele la care participa persoana data
        """
        if self.__people_repository.find_person_by_id(person_id) is None:
            raise self.__person_exception("Persoana nu exista!")
        sign_list = self.__sign_repository.show_sign_list()
        person_sign_list = []
        for i in range(len(sign_list)):
            if sign_list[i].person_id == person_id:
                person_sign_list.append(self.__event_repository.find_event_by_id(sign_list[i].event_id))
        return person_sign_list
    
    def print_event_signs(self, event_id):
        """Functia primeste ca parametru id-ul unui eveniment si apoi verifica daca acesta exista in lista cu evenimente. Daca da, se creeaza o lista goala in care
        vor fi memorate persoanele care participa la eveniment, iar aceasta se va returna

        Args:
            event_id (int): id-ul evenimentului

        Raises:
            self.__event_exception: eroarea aruncata daca evenimentul nu exista

        Returns:
            list: lista cu persoanele care partiicipa la eveniment
        """
        if self.__event_repository.find_event_by_id(event_id) is None:
            raise self.__event_exception("Evenimentul nu exista!")
        sign_list = self.__sign_repository.show_sign_list()
        event_sign_list = []
        for i in range(len(sign_list)):
            if sign_list[i].event_id == event_id:
                event_sign_list.append(self.__people_repository.find_person_by_id(sign_list[i].person_id))
        return event_sign_list
    
    def sort_list(self, person_id):
        """Functia primeste ca parametru id-ul unei persoane. Apoi se verifica si se creeaza o lista cu toate evenimentele la care participa. Lista
        este sortata dupa data la care au loc evenimentele, apoi ele sunt sortate alfabetic dupa descriere.

        Args:
            person_id (int): id-ul persoanei

        Returns:
            list: o lista ordonata cu evenimentele la care participa persoana 
        """
        sign_list = self.__create_event_sort_dtos(person_id)
        sign_list = sorted(sign_list, key=lambda x: (x.event_month, x.event_day, x.event_descr))            
        return sign_list
      
    def __create_event_sort_dtos(self, person_id):
        """Creeaza lista de dto-uri si o returneaza

        Args:
            person_id (int): id-ul persoanei careia i se sorteaza lista de evenimente

        Returns:
            list: lista de dto-uri
        """
        event_dtos = []
        for event in self.print_person_signs(person_id):
            dto = EventSortDTOAssembler.create_event_sort_dto(event)
            event_dtos.append(dto)
        return event_dtos
                     
    def people_participation(self):
        """Sorteaza lista de dto-uri in functie de nr de evenimente la care s-a insris o persoana si returneaza lista ce persoanele
        care participa la cele mai multe evenimente.

        Returns:
            list: lista de dto-uri
        """
        people_dtos = self.__create_people_dtos()
        people_dtos = sorted(people_dtos, key=lambda x:x.number_of_events)
        return self.find_most_participants(people_dtos)
        
    def find_most_participants(self, sign_list):
        """Primeste o lista de dto-uri din care sunt eliminate persoanele care nu participa la cele mai multe evenimente.

        Args:
            sign_list (list): lista de dto-uri cu toate persoanele

        Returns:
            list: lista de dto-uri doar cu persoanele care participa la cele mai multe evenimente
        """
        if sign_list[len(sign_list) -1 ].number_of_events == sign_list[0].number_of_events:
            return sign_list
        return self.find_most_participants(sign_list[1:])
    
    def __create_people_dtos(self):
        """Creaza o lista de dto-uri.

        Returns:
            list: lista de dto-uri
        """
        people_dtos = []
        for person in self.__people_repository.find_all():
            sign_list = self.print_person_signs(person.personID)
            dto = PeopleDTOAssembler.create_person_dto(person, sign_list)
            people_dtos. append(dto)
        return people_dtos
    
    
    def first20(self):
        """Returneaza o lista cu primele 20% evenimente in functie de nr de participanti.

        Returns:
            list: lista de dto-uri sortata cu primele 20% evenimente
        """
        events_dtos = self.__create_events_dtos()
        events_dtos = sorted(events_dtos, key=lambda x:x.number_of_participants)
        nr = int(0.2 * len(events_dtos))
        return self.generate_list(events_dtos, nr)
    
        
    def generate_list(self, sign_list, lngt):
        """Sterge elemente din coada listei pana cand ea ajunge la lungimea data.

        Args:
            sign_list (list): lista de dto-uri
            lngt (int): lungimea listei

        Returns:
            list: lista de lungime 'lngt'
        """
        if len(sign_list) == lngt:
            return sign_list
        return self.generate_list(sign_list[1:], lngt)
        
    def __create_events_dtos(self):
        """Creeaza o lista de dto-uri

        Returns:
            list: lista de dto-uri
        """
        events_dtos = []
        for event in self.__event_repository.find_all_events():
            sign_list = self.print_event_signs(event.ID)
            dto = EventDTOAssembler.create_event_dto(event, sign_list)
            events_dtos.append(dto)
        return events_dtos
    
    def cancel_sign(self, person_id, event_id):
        """Anuleaza inscrierea unei persoane la un eveniment

        Args:
            person_id (int): id-ul persoanei
            event_id (int): id-ul evenimentului
        """
        self.__sign_repository.cancel_sign(person_id, event_id)