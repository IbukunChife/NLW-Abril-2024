from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.attendees_handler import AttendeesHandler
from src.errors.error_handler import handler_error

attendees_route_bp = Blueprint("attendees_route", __name__)


@attendees_route_bp.route("/events/<event_id>/register", methods=["GET"])
def create_attendees(event_id):
    try:
        http_request = HttpRequest(
            param={"event_id": event_id}, body=request.json)
        attendees_handler = AttendeesHandler()

        http_response = attendees_handler.registry(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handler_error(exception)
        return jsonify(http_response.body), http_response.status_code


@attendees_route_bp.route("/attendees/<attendee_id>/badge", methods=["GET"])
def get_attendees_badge(attendee_id):
    try:
        attendee_handler = AttendeesHandler()
        http_request = HttpRequest(param={"attendee_id": attendee_id})

        http_response = attendee_handler.find_attendees_badge(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handler_error(exception)
        return jsonify(http_response.body), http_response.status_code


@attendees_route_bp.route("/events/<event_id>/attendees", methods=["GET"])
def get_attendees(event_id):
    try:
        attendee_handler = AttendeesHandler()
        http_request = HttpRequest(param={"event_id": event_id})

        http_response = attendee_handler.find_attendees_from_event(
            http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handler_error(exception)
        return jsonify(http_response.body), http_response.status_code
