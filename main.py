from Service.people_service import PeopleService
from UI.console import Console
from Service.events_service import EventsService
from Domain.validators import EventException, EventValidator, PersonException, PersonValidator
from Service.sign_service import SignSerivce
from Repository.text_file_repository import EventTextFile, PeopleTextFile
from Repository.sign_text_file_repository import SignTextFile


def main():
    person_exception = PersonException
    person_validator = PersonValidator()
    event_exception = EventException
    event_validator = EventValidator()
    people_repository = PeopleTextFile(r"C:\Users\teodo\Desktop\New folder\Organizare Evenimente\Data\persoane",
                                       person_validator)
    events_repository = EventTextFile(r"C:\Users\teodo\Desktop\New folder\Organizare Evenimente\Data\evenimente",
                                      event_validator)
    sign_repository = SignTextFile(r"C:\Users\teodo\Desktop\New folder\Organizare Evenimente\Data\inscrieri",
                                   people_repository, events_repository)
    events_service = EventsService(events_repository, event_exception, event_validator)
    people_service = PeopleService(people_repository, person_exception, person_validator)
    sign_service = SignSerivce(sign_repository, people_repository, events_repository, person_exception, event_exception)
    console = Console(people_service, events_service, sign_service)
    console.run_console()
    console.options()


if __name__ == "__main__":
    main()
