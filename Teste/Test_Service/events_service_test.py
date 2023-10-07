import unittest
from Service.events_service import EventsService
from Repository.events_repository import EventRep
from Domain.validators import EventException, EventValidator
from Domain.entities import Event

event_validator = EventValidator()
event_exception = EventException
events_repository = EventRep()
events_service = EventsService(events_repository, event_exception, event_validator)

class TestEventService(unittest.TestCase):
    def setup(self):
        events_service.add_event(1, "03.10", 3, "Oktoberfest")
        events_service.add_event(2, "10.07", 5, "Rockstadt")
        events_service.add_event(3, "05.04", 7, "Festivalul gratarelor")
        events_service.add_event(4, "05.04", 4, "Concursul de vopsit oua")
        
    def clear_test(self):
        events_repository.delete_all_events()
    
    def test_check_if_event_exist(self):
        self.setup()
        self.assertEqual(events_service.check_if_event_exists(3), Event(3, "05.04", 7, "Festivalul gratarelor"))
        self.assertIsNone(events_service.check_if_event_exists(10))
        self.clear_test()
        
        
    def test_find_event_by_description(self):
        self.setup()
        self.assertEqual(events_service.find_event_by_description("Rockstadt"), [Event(2, "10.07", 5, "Rockstadt")])
        with self.assertRaises(event_exception):
            events_service.find_event_by_description("Concert BAZOOKA")
        self.clear_test()
        
    def test_get_all_events(self):
        self.setup()
        all_events_list = [Event(1, "03.10", 3, "Oktoberfest"),
                           Event(2, "10.07", 5, "Rockstadt"),
                           Event(3, "05.04", 7, "Festivalul gratarelor"),
                           Event(4, "05.04", 4, "Concursul de vopsit oua"),
                           ]
        self.assertEqual(events_service.get_all_events(), all_events_list)
        self.clear_test()
    
    def test_add_event(self):
        self.setup()
        add_event_list = [Event(1, "03.10", 3, "Oktoberfest"),
                          Event(2, "10.07", 5, "Rockstadt"),
                          Event(3, "05.04", 7, "Festivalul gratarelor"),
                          Event(4, "05.04", 4, "Concursul de vopsit oua"),
                          Event(7, "03.12", 7, "Inaugurarea partiei")]
        self.assertEqual(events_service.add_event(7, "03.12", 7, "Inaugurarea partiei"), add_event_list)
        self.clear_test()
        
    def test_delete_event(self):
        self.setup()
        delete_event_list = [Event(1, "03.10", 3, "Oktoberfest"),
                           Event(2, "10.07", 5, "Rockstadt"),
                           Event(4, "05.04", 4, "Concursul de vopsit oua"),
                           ]
        self.assertEqual(events_service.delete_event(3), delete_event_list)
        self.clear_test()
    
    def test_update_event(self):
        self.setup()
        update_event_list = [Event(1, "03.10", 3, "Oktoberfest"),
                          Event(2, "10.07", 5, "Rockstadt"),
                          Event(3, "05.04", 7, "Festivalul gratarelor"),
                          Event(4, "05.04", 7, "Concursul de vopsit oua")
                          ]
        self.assertEqual(events_service.update_event(4, "05.04", 7, "Concursul de vopsit oua"), update_event_list)
        self.clear_test()