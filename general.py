# -*- coding: utf-8 -*-
from dataclasses import dataclass


@dataclass(slots=True)
class General:
    """Base class for all other entity classes in the project"""

    code: int = 0


#
# More traditional way of Pyhton class implementation
#
# class General:
#     """Base class for all other entity classes in the project"""

#     def __init__(self, code=0):
#         self.code = code

#     @property
#     def code(self):
#         return self.__code

#     @code.setter
#     def code(self, code):
#         self.__code = code
