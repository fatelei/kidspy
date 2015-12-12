# -*- coding: utf8 -*-
"""
    kids
    ~~~~

    Kids Python Client Library.
"""

__version__ = "1.0.0"


from .log_handler import KidsHandler
from .utils import setup_kids

__all__ = [
    "KidsHandler",
    "setup_kids"
]
