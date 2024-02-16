from sqlalchemy import Column, String, Integer

from utils import db


class PlaceModel(db.Model):
    __tablename__ = "place"
    id_place = Column(
        Integer,
        primary_key=True,
        unique=True,
        nullable=False
    )
    department_name = Column(
        String,
        unique=True,
        nullable=False,
    )
    department_code = Column(
        Integer,
        unique=True,
        nullable=False
    )
    town_name = Column(
        String,
        nullable=False,
    )
    town_code = Column(
        Integer,
        nullable=False
    )
    description = Column(
        String(250),
        nullable=True,
    )
    fk_case_id = Column(
        Integer,
        nullable=False
    )