#!/usr/bin/python3
"""A state class that inherits from BaseModel"""
from models.base_model import BaseModel

class Review(BaseModel):
    """Represents a review
    Attributes: 
        place_id (str)
        user_id (str)
        text (str)"""
    place_id = ""
    user_id = ""
    text = ""
    
    
    
    
