from Domain.validators import PersonEventException

class EventRepException(PersonEventException):
    pass

class EventRep:
    def __init__(self):
        self.__event_list = {}
        
    def save_event(self, event):
        if self.find_event_by_id(event.ID) is not None:
            raise EventRepException("Id duplicat!")
        self.__event_list[event.ID] = event
    
    def find_event_by_id(self, event_id):
        try:
            return self.__event_list[event_id]
        except KeyError:
            return None
    
    def delete_event_by_id(self, event_id):
        if self.find_event_by_id(event_id) is None:
            raise EventRepException("Evenimentul nu exista!")
        del self.__event_list[event_id]
    
    def find_all_events(self):
        return list(self.__event_list.values())
    
    def update_event(self, event):
        if self.find_event_by_id(event.ID) is None:
            raise EventRepException("Evenimentul nu exista!")
        self.__event_list[event.ID] = event
        
    def delete_all_events(self):
        self.__event_list.clear()

