import pytest
from src.models.settings.connection import db_connection_handler
from .attendees_repository import AttendeesRepository

db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="Novo registro em branco de dados")
def test_insert_attendee():
    event_id = "meu-uuid-e-nois"
    attendees_info = {
        "uuid": "meu-uuid-attendee",
        "name": "attendee name",
        "email": "email@email.com",
        "event_id": event_id
    }

    attendee_Repository = AttendeesRepository()
    response = attendee_Repository.insert_attendee(attendees_info)
    print(response)


@pytest.mark.skip(reason="......")
def test_get_attendee_badge_by_id():
    attendee_id = "meu-uuid-attendee"
    attendee_repository = AttendeesRepository()
    response = attendee_repository.get_attendee_badge_by_id(attendee_id)
    print(response)
    print(response.title)
