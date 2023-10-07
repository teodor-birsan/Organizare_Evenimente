import unittest
from Domain.validators import EventValidator, PersonValidator, ValidatorException
from Domain.entities import Event, Person

event_validator = EventValidator()
person_validator = PersonValidator()

person = Person(1, "io", "adress")
event1 = Event(1, "01/01", 3, "descr")
event2 = Event(2, "01.13", 3, "descr")
event3 = Event(3, "32.01", 3, "descr")
event4 = Event(4, "30.02", 3, "descr")
event5 = Event(5, "32.04", 3, "descr")


class TestValidators(unittest.TestCase):
    def test_person_validator(self):
        with self.assertRaises(ValidatorException):
            person_validator.validate(person)
    def test_event_validator(self):
        with self.assertRaises(ValidatorException):
            event_validator.validate(event1)
        with self.assertRaises(ValidatorException):
            event_validator.validate(event2)
        with self.assertRaises(ValidatorException):
            event_validator.validate(event3)
        with self.assertRaises(ValidatorException):
            event_validator.validate(event4)
        with self.assertRaises(ValidatorException):
            event_validator.validate(event5)       
    
        