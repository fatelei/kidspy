# -*- coding: utf8 -*-
"""
    test.test_kids
    ~~~~~~~~~~~~~~

    Kids unittest.
"""

import logging
import logging.config
import unittest


class TestKids(unittest.TestCase):

    def test_setup_kids(self):
        from kids import setup_kids, KidsHandler
        root = logging.getLogger()
        root.handlers = []
        setup_kids()
        self.assertIsInstance(root.handlers[1], KidsHandler)

    def test_add_kids_handler(self):
        from kids import KidsHandler
        test = logging.getLogger('test')
        handler = KidsHandler()
        test.addHandler(handler)
        self.assertIn(handler, test.handlers)

    def test_setup_kids_via_dictconfig(self):
        from kids import KidsHandler
        logging.config.dictConfig({
            "version": 1,
            "handlers": {
                "kids": {
                    "class": "kids.KidsHandler"
                }
            },
            "loggers": {
                "test": {
                    "handlers": ["kids"]
                }
            }
        })
        test = logging.getLogger("test")
        self.assertIsInstance(test.handlers[0], KidsHandler)

    def test_log_with_kids(self):
        from kids import KidsHandler
        from redis import StrictRedis
        cli = StrictRedis(port=6379, host="localhost")
        p = cli.pubsub()
        p.subscribe("test")
        p.get_message()
        test = logging.getLogger("test")
        test.handlers = []
        handler = KidsHandler(port=6379, host="localhost")
        test.addHandler(handler)
        test.info("test")
        rst = p.get_message()
        self.assertIn("test", rst["data"])
