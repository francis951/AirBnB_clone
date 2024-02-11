#!/usr/bin/python3
"""Defines a class State that inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """Class that defines properties of State."""

    name = ""

    def __init__(self, *args, **kwargs):
        """Creates new instances of State."""
        super().__init__(*args, **kwargs)
