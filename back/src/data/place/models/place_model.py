from sqlalchemy import Column, String, Integer

from utils import db


class PlaceModel(db.Model):
    __tablename__ = "place"
    id = Column(
        Integer,
        primary_key=True,
        unique=True,
        nullable=False
    )
    message = Column(String(100))