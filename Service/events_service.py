from Domain.entities import Event


class EventsService:
    def __init__(self, events_repository, event_exception, event_validator):
        self.__events_repository = events_repository
        self.__event_validator = event_validator
        self.__event_exception = event_exception

    def get_all_events(self):
        return self.__events_repository.find_all_events()
    
    def add_event(self, event_id, date, time, description):
        event = Event(event_id, date, time, description)
        self.__event_validator.validate(event)
        self.__events_repository.save_event(event)
        return self.get_all_events()
    
    def delete_event(self, event_id):
        self.__events_repository.delete_event_by_id(event_id)
        return self.get_all_events()
        
    def update_event(self, event_id, date, time, description):
        event = Event(event_id, date, time, description)
        self.__events_repository.update_event(event)
        return self.get_all_events()
        
    def check_if_event_exists(self, event_id):
        """Functia primeste ca parametru id-ul unui eveniment si il cauta in dictionar. Daca il gaseste va returna obiectul din dictionar cu cheia "event_id".
        Daca nu, ea returneaza 'None'.

        Args:
            event_id (str): id-ul evenimentului pt care se verifca existenta in dictionar

        Returns:
            object: returneaza obiectul Event(), daca exista. Altfel returneaza None
        """
        return self.__events_repository.find_event_by_id(event_id)
    
    def find_event_by_description(self, description):
        """Functia primeste ca parametru descrierea unui eveniment si retruneaza intr-o lista toate evenimentele cu acea descriere. Daca nu sunt evenimente cu
        descrierea data, functia returneaza None.

        Args:
            description (str): descrierea evenimentului

        Returns:
            list: lista cu evenimente care au descrierea data
        """
        event_list = self.__events_repository.find_all_events()
        desc_list = []
        for i in range(len(event_list)):
            if event_list[i].description == description:
                desc_list.append(event_list[i])
        if len(desc_list) == 0:
            raise self.__event_exception("Nu s-au gasit evenimente cu descrierea data!")
        return desc_list    