#!/usr/bin/python3
""" Review Class that
representation """

from models.base_model import BaseModel


class Review(BaseModel):

    """Initialize review class
    instance
    of basemodel class"""

    place_id = ''
    user_id = ''
    text = ''
