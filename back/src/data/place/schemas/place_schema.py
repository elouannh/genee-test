"""Schema for serializing/deserializing a PlaceModel"""

from data.place.models.place_model import PlaceModel
from utils.base_schema import BaseSchema


class PlaceSchema(BaseSchema):
    class Meta:
        model = PlaceModel
        load_instance = True