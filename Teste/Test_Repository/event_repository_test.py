import unittest
from Repository.events_repository import EventRep, EventRepException
from Domain.entities import Event

event_repository = EventRep()
event_repository_exception = EventRepException

class TestEventRepository(unittest.TestCase):
    def setup(self):
        event_repository.save_event(Event(1, "03.09", 5, "event1"))
        event_repository.save_event(Event(2, "03.04", 3, "event2"))    

    def test_save_event(self):
        self.setup()
        self.assertIsNone(event_repository.save_event(Event(3, "03.03", 4, "event3")))
        with self.assertRaises(event_repository_exception):
            event_repository.save_event(Event(1, "01.01", 3, "event4"))
        event_repository.delete_all_events()
        
    def test_delete_event_by_id(self):
        self.setup()
        self.assertIsNone(event_repository.delete_event_by_id(1))
        with self.assertRaises(event_repository_exception):
            event_repository.delete_event_by_id(7)
        event_repository.delete_all_events()
            
    def test_update_event(self):
        self.setup()
        self.assertIsNone(event_repository.update_event(Event(1, "01.01", 3, "new_event")))
        with self.assertRaises(event_repository_exception):
            event_repository.update_event(Event(5, "01.01", 1, "event")) 
        event_repository.delete_all_events()
            
    def test_find_event(self):
        self.setup()
        self.assertEqual(event_repository.find_event_by_id(1), Event(1, "03.09", 5, "event1"))
        self.assertIsNone(event_repository.find_event_by_id(5))
        event_repository.delete_all_events()
        