import unittest
from Service.people_service import PeopleService
from Domain.validators import  PersonException, PersonValidator
from Repository.people_repository import PeopleRep
from Domain.entities import Person



people_validator = PersonValidator()
people_exception = PersonException
people_reposiotry = PeopleRep()
people_service = PeopleService(people_reposiotry, people_exception, people_validator)

class TestPeopleService(unittest.TestCase):
    def setup(self):
        people_service.add_person(1, "Teodor", "teodor_15@gmail.com")
        people_service.add_person(2, "Alex", "alex.2003@gmail.com")
        people_service.add_person(3, "Teodor", "teodor.1404@gmail.com")
        
    def clear_test(self):
        people_reposiotry.delete_all_people()
          
    def test_check_if_exists(self):
        self.setup()
        self.assertEqual(people_service.check_if_exists(1), Person(1, "Teodor", "teodor_15@gmail.com"))
        self.assertIsNone(people_service.check_if_exists(5))
        self.clear_test()

    def test_find_people_by_name(self):
        self.setup()
        self.assertEqual(people_service.find_people_by_name("Teodor"), [Person(1, "Teodor", "teodor_15@gmail.com"), Person(3, "Teodor", "teodor.1404@gmail.com")])
        with self.assertRaises(people_exception):
            people_service.find_people_by_name("Ion")
        self.clear_test()

    def test_get_all_people(self):
        self.setup()
        all_people_list = [Person(1, "Teodor", "teodor_15@gmail.com"),
                           Person(2, "Alex", "alex.2003@gmail.com"),
                           Person(3, "Teodor", "teodor.1404@gmail.com")]
        self.assertEqual(people_service.get_all_people(), all_people_list)
        self.clear_test()
        
    def test_add_person(self):
        self.setup()
        add_person_list = [Person(1, "Teodor", "teodor_15@gmail.com"),
                           Person(2, "Alex", "alex.2003@gmail.com"),
                           Person(3, "Teodor", "teodor.1404@gmail.com"),
                           Person(7, "Gabriel", "gabi225@gmail.com")]
        self.assertEqual(people_service.add_person(7, "Gabriel", "gabi225@gmail.com"), add_person_list)
        self.clear_test()
    
    def test_delete_person(self):
        self.setup()
        self.assertEqual(people_service.delete_person(2), [Person(1, "Teodor", "teodor_15@gmail.com"), Person(3, "Teodor", "teodor.1404@gmail.com")])
        self.clear_test()
        
    def test_update_person(self):
        self.setup()
        update_person_list = [Person(1, "Teodor", "teodor_15@gmail.com"),
                              Person(2, "Alex", "alex.2003@gmail.com"),
                              Person(3, "Teodor", "te0d0r.1404@gmail.com")]
        self.assertEqual(people_service.update_person(3, "Teodor", "te0d0r.1404@gmail.com"), update_person_list)
        self.clear_test()