import unittest
from Repository.people_repository import PeopleRep, PeopleRepException
from Domain.entities import Person


person_repository = PeopleRep()
repository_exception = PeopleRepException

class TestPeopleRepository(unittest.TestCase):
    def setup(self):
        person_repository.save_person(Person(1, "person1", "adress"))
        person_repository.save_person(Person(2, "person2", "adress"))       

    def test_save_person(self):
        self.setup()
        self.assertIsNone(person_repository.save_person(Person(3, "person3", "adress")))
        with self.assertRaises(repository_exception):
            person_repository.save_person(Person(1, "person1", "adress"))
        person_repository.delete_all_people()
            
    def test_delete_person_by_id(self):
        self.setup()
        self.assertIsNone(person_repository.delete_person_by_id(1))
        with self.assertRaises(repository_exception):
            person_repository.delete_person_by_id(10)
        person_repository.delete_all_people()
            
    def test_update_person(self):
        self.setup()
        self.assertIsNone(person_repository.update_person(Person(1, "person2b", "person2badress")))
        with self.assertRaises(repository_exception):
            person_repository.update_person(Person(3, "person3", "adress"))
        person_repository.delete_all_people()
    
    def test_find_person(self):
        self.setup()
        self.assertEqual(person_repository.find_person_by_id(1), Person(1, "person1", "adress"))
        self.assertIsNone(person_repository.find_person_by_id(3))
        person_repository.delete_all_people()
        
            
    