#!/usr/bin/python3
"""A state class that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Public class attribute : state_id & name"""

    state_id = ""
    name = ""
