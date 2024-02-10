#!/usr/bin/python3

from .base_model import BaseModel


class User(BaseModel):
    """user class that inherits BaseModel class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    
    def __init__(self, *args, **kwargs):
        """instance initialization"""
        super().__init__(*args, **kwargs)
        for key, value in kwargs.items():
            if key in ['email', 'password', 'first_name', 'first_name']
            setattr(self, key, value)
