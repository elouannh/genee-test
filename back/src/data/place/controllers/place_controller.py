""" Routes for the endpoint 'place'"""

from flask import Blueprint, request
from marshmallow import ValidationError

from data.place.models import PlaceModel
from data.place.schemas import PlaceSchema
from utils import db

NAME = 'place'

place_blueprint = Blueprint(f"{NAME}_place_blueprint", __name__)


@place_blueprint.get(f"/{NAME}/<int:id>")
def get_place(id: str):
    """GET route code goes here"""
    entity: PlaceModel = db.session.query(PlaceModel).get(id)
    if entity is None:
        return "Goodbye World.", 404
    return entity.message, 200


@place_blueprint.post(f"/{NAME}/")
def post_place():
    """POST route code goes here"""
    payload = request.get_json()
    try:
        entity: PlaceModel = PlaceModel().load(payload)
    except ValidationError as error:
        return f"The payload does't correspond to a valid PlaceModel: {error}", 400
    db.session.add(entity)
    db.session.commit()
    return PlaceModel().dump(entity), 200


@place_blueprint.delete(f"/{NAME}/<int:id>")
def delete_place(id: str):
    """DELETE route code goes here"""
    return "Unimplemented", 501


@place_blueprint.put(f"/{NAME}/<int:id>")
def put_place(id: str):
    """PUT route code goes here"""
    return "Unimplemented", 501


@place_blueprint.patch(f"/{NAME}/<int:id>")
def patch_place(id: str):
    """PATCH route code goes here"""
    return "Unimplemented", 501