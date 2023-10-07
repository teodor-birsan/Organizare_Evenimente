class PersonEventException(Exception):
    pass

class PersonException(PersonEventException):
    pass

class EventException(PersonEventException):
    pass

class ValidatorException(PersonEventException):
    pass

class SignException(PersonEventException):
    pass

class EventValidator:
    def validate(self, event):
        date = event.date.split('.')
        if len(date) < 2 or date[1] > '12' or (date[1] in ['01', '03', '05', '07', '08', '10', '12'] and date[0] > '31') or (date[1] == '02' and date[0] > '28') or (date[1] in ['04', '06', '09', '11'] and date[0] > '30'):
            raise ValidatorException("Data invalida!")
class PersonValidator:
    def validate(self, person):
        if len(person.name) < 3:
            raise ValidatorException("Numele nu poate avea mai putin de trei caractere!")