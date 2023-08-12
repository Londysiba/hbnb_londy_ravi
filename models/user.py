#!/usr/bin/python3
"""A state class that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Public class attributes are
    Email, Password, First_name, and Lat_name"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
