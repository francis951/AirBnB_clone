#!/usr/bin/python3
"""Creates a unique file storage for the app.
"""

from models.engine.file_storage import FileStorage
from .base_model import BaseModel


classes = {
    'BaseModel': BaseModel,
    # Add other models here...
}

storage = FileStorage()
storage.reload()