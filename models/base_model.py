#!/usr/bin/python3
"""
A module that implements the BaseModel class
"""
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """

    def __init__(self,*args, **kwargs):