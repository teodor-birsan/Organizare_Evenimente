import unittest
from Domain.entities import Event, Person

person = Person(1, "person", "adress")
event = Event(1, "01.01", 3, "descr")

class TestEntities(unittest.TestCase):
    def test_print_person(self):
        prs_array = str(person)
        self.assertEqual(prs_array, "ID: 1, Nume: person, Adresa: adress \n")\
            
    def test_print_event(self):
        event_array = str(event)
        self.assertEqual(event_array, "ID: 1, Data (zz/ll): 01.01, Timp (in zile): 3, Descriere: descr \n")