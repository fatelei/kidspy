# -*- coding: utf8 -*-
"""
    kids.utils
    ~~~~~~~~~~

    Kids utilities.
"""

import logging

from .log_handler import KidsHandler


def setup_kids(level=logging.INFO,
               port=3388,
               host="localhost",
               topic=None):
    """Setup kids, add `KidsHandler` to root logger.

    :param int level: Log level
    :param int port: Kids server port
    :param str host: Kids server hostname
    ;param str topic: Kids topic
    """
    root = logging.getLogger()
    if not root.handlers:
        logging.basicConfig(level=level)  # Here add a streamhandler.
    handler = KidsHandler(port=port,
                          host=host,
                          topic=topic)
    handler.setLevel(level)
    root.addHandler(handler)
