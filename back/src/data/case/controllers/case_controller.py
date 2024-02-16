""" Routes for the endpoint 'case'"""

from flask import Blueprint, request
from marshmallow import ValidationError

from data.case.models import CaseModel
from data.case.schemas import CaseSchema
from data.case.services import CaseService
from utils import db

NAME = 'case'

case_blueprint = Blueprint(f"{NAME}_case_blueprint", __name__)


@case_blueprint.get(f"/{NAME}/<int:id>")
def get_case(id: str):
    """GET route code goes here"""
    entity: CaseModel = db.session.query(CaseModel).get(id)
    if entity is None:
        return "Case not found.", 404
    return entity.message, 200


@case_blueprint.post(f"/{NAME}/")
def post_case():
    """POST route code goes here"""
    payload = request.get_json()

    passing = CaseService.is_valid(payload)
    if len(passing) > 0:
        joined = '\n'.join(map(lambda x: f'- {x}', passing))
        return f"The playload doesn't correspond to a valid form submit.\n{joined}", 400

    return payload, 200


@case_blueprint.delete(f"/{NAME}/<int:id>")
def delete_case(id: str):
    """DELETE route code goes here"""
    return "Unimplemented", 501


@case_blueprint.put(f"/{NAME}/<int:id>")
def put_case(id: str):
    """PUT route code goes here"""
    return "Unimplemented", 501


@case_blueprint.patch(f"/{NAME}/<int:id>")
def patch_case(id: str):
    """PATCH route code goes here"""
    return "Unimplemented", 501