#!/usr/bin/python3
"""Defines a class City that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class that defines properties of City"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Creates new instances of City."""
        super().__init__(*args, **kwargs)
