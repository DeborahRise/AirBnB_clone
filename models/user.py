#!/usr/bin/python3
""" User representation and
instantiation """

from models.base_model import BaseModel


class User(BaseModel):
    """Initialize user class
    instance
    of basemodel class"""

    email = ''
    password = ''
    first_name = ''
    last_name = ''
