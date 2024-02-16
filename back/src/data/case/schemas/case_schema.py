"""Schema for serializing/deserializing a CaseModel"""

from data.case.models.case_model import CaseModel
from utils.base_schema import BaseSchema


class CaseSchema(BaseSchema):
    class Meta:
        model = CaseModel
        load_instance = True