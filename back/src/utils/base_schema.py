from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from utils import db


class BaseSchema(SQLAlchemyAutoSchema):
    """
    Base schema auto-attaching the session and keeping track of media resources during load()
    """

    class Meta:
        required = True

    def __init__(self, *args, **kwargs):
        if not kwargs.get('session'):
            kwargs['session'] = db.session

        super().__init__(*args, **kwargs)