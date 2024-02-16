from utils import db
from data.case.models import CaseModel
from data.case.schemas import CaseSchema
from data.place.models import PlaceModel
from data.place.schemas import PlaceSchema


class CaseService:
    @staticmethod
    def is_valid(json_obj) -> list[str]:
        """Returns a boolean designating if a posted json can be stored properly."""
        errors: list[str] = []

        if 'case_name' in json_obj:
            if len(json_obj['case_name']) < 4:
                errors.append("Case name must contain at least 4 characters.")
        else:
            errors.append("Missing case_name field.")

        if 'department_name' in json_obj:
            if len(json_obj['department_name']) < 4:
                errors.append("Department name must contain at least 4 characters.")
        else:
            errors.append("Missing department_name field.")

        if 'town_name' in json_obj:
            if len(json_obj['town_name']) < 4:
                errors.append("Town name must contain at least 4 characters.")
        else:
            errors.append("Missing town_name field.")

        return errors

    @staticmethod
    def register_case(json_obj):
        case_entity: CaseSchema = CaseSchema().load({ "case_name": json_obj['case_name'] })

        db.session.add(case_entity)
        db.session.commit()

        return case_entity
