import unittest
from Service.sign_service import SignSerivce
from Repository.sign_repository import SignPeople
from Repository.people_repository import PeopleRep
from Repository.events_repository import EventRep
from Domain.validators import (EventException, EventValidator, PersonException, PersonValidator,
    SignException)
from Domain.entities import Event, Person, Sign
from Service.people_service import PeopleService
from Service.events_service import EventsService
from Domain.dto import EventSortDTO, PeopleDTO

sign_exception = SignException
event_exception = EventException
person_exception = PersonException
event_repository = EventRep()
people_repository = PeopleRep()
sign_repository = SignPeople(people_repository, event_repository)
sign_service = SignSerivce(sign_repository, people_repository, event_repository, person_exception, event_exception)
person_validator = PersonValidator()
people_service = PeopleService(people_repository, person_exception, person_validator)
event_validator = EventValidator()
events_service = EventsService(event_repository, event_exception, event_validator)


class TestSignService(unittest.TestCase):
    def setup(self):
        people_service.add_person(1, "person1", "adress")
        people_service.add_person(2, "person2", "adress")
        people_service.add_person(3, "person3", "adress")
        events_service.add_event(1, "01.01", 3, "event1")
        events_service.add_event(2, "20.12", 4, "event2")
        sign_service.sign_person_to_event(1, 1)
        sign_service.sign_person_to_event(1, 2)
        sign_service.sign_person_to_event(2, 1)
        sign_service.sign_person_to_event(2, 2)
        sign_service.sign_person_to_event(3, 1)
        
    def clear_test(self):
        people_repository.delete_all_people()
        event_repository.delete_all_events()
        sign_repository.delete_all_signs()
        
    def test_print_person_signs(self):
        self.setup()
        with self.assertRaises(PersonException):
            sign_service.print_person_signs(4)
        self.assertEqual(sign_service.print_person_signs(1), [Event(1, "01.01", 3, "event1"), Event(2, "20.12", 4, "event2")])
        self.clear_test()
        
    def test_print_event_signs(self):
        self.setup()
        with self.assertRaises(EventException):
            sign_service.print_event_signs(3)
        self.assertEqual(sign_service.print_event_signs(2), [Person(1, "person1", "adress"), Person(2, "person2", "adress")])
        self.clear_test()
        
    def test_sort_list(self):
        self.setup()
        self.assertEqual(sign_service.sort_list(1), [EventSortDTO("01", "01", "event1"), EventSortDTO("20", "12", "event2")])
        self.clear_test()
    
    def test_people_participation(self):
        self.setup()
        self.assertEqual(sign_service.people_participation(), [PeopleDTO("person1", 2), PeopleDTO("person2", 2)])
        self.clear_test()
        
    def test_first20(self):
        self.setup()
        self.assertEqual(sign_service.first20(), [])
        self.clear_test()
    
    def test_cancel_sign(self):
        self.setup()
        self.assertIsNone(sign_service.cancel_sign(1, 1))
        self.clear_test()
        
        