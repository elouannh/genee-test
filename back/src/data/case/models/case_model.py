from sqlalchemy import Column, String, Integer

from utils import db


class CaseModel(db.Model):
    __tablename__ = "case"
    id_case = Column(
        Integer,
        primary_key=True,
        unique=True,
        nullable=False
    )
    case_name = Column(
        String(100),
        nullable=False
    )