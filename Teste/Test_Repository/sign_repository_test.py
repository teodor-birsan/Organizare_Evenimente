import unittest
from Repository.sign_repository import SignPeople, SignPeopleRepException
from Repository.people_repository import PeopleRep
from Repository.events_repository import EventRep
from Domain.entities import Event, Person, Sign

event_repository = EventRep()
people_repository = PeopleRep()
sign_repository = SignPeople(people_repository, event_repository)

class TestSignRepository(unittest.TestCase):
    def setup(self):
       event_repository.save_event(Event(1, "01.01", 3, "event1"))
       event_repository.save_event(Event(2, "02.02", 5, "event3"))
       event_repository.save_event(Event(3, "03.03", 6, "event3"))
       people_repository.save_person(Person(1, "person1", "adress"))
       people_repository.save_person(Person(2, "person2", "adress"))
       sign_repository.sign_people(Sign(1, 1))
       sign_repository.sign_people(Sign(2, 3))
       sign_repository.sign_people(Sign(1, 3))

    def clear_test(self):
        event_repository.delete_all_events()
        people_repository.delete_all_people()
        sign_repository.delete_all_signs()
        
    def test_sign_people(self):
        self.setup()
        with self.assertRaises(SignPeopleRepException):
            sign_repository.sign_people(Sign(1, 4))
            sign_repository.sign_people(Sign(5, 1))
        with self.assertRaises(SignPeopleRepException):
            sign_repository.sign_people(Sign(1, 1))
        self.assertIsNone(sign_repository.sign_people(Sign(1, 2)))
        self.clear_test()
        
    def test_find_sign(self):
        self.setup()
        with self.assertRaises(SignPeopleRepException):
            sign_repository.find_sign(1, 5)
            sign_repository.find_sign(3, 1)
        self.assertEqual(sign_repository.find_sign(1, 1), Sign(1, 1))
        self.assertIsNone(sign_repository.find_sign(2, 1))
        self.clear_test()
        
    def test_cancel_sign(self):
        self.setup()
        with self.assertRaises(SignPeopleRepException):
            sign_repository.cancel_sign(3, 1)
            sign_repository.cancel_sign(1, 5)
        with self.assertRaises(SignPeopleRepException):
            sign_repository.cancel_sign(1, 2)
        self.assertIsNone(sign_repository.cancel_sign(1, 1))
        self.clear_test()
        
    def test_show_sign_list(self):
        self.setup()
        sign_list = [Sign(1, 1), Sign(2, 3), Sign(1, 3)]
        self.assertEqual(sign_repository.show_sign_list(), sign_list)
        self.clear_test()        
    
              