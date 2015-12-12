.. _tutorial:

Tutorial
========

There are some methods to use *kids*.

Setup for root logger
---------------------

You can setup for program widely. via::

  # -*- coding: utf8 -*-

  import logging
  from kids import setup_kids

  setup_kids(level=logging.INFO,
             port=3388,
             host="localhost",
             topic="test")

Setup for own logger
--------------------

You can do this like::

  # -*- coding: utf8 -*-

  import logging
  from kids import KidsHandler

  test = logging.getLogger('test')

  handler = KidsHandler(port=3388,
                        host="localhost",
                        topic="test")
  test.addHandler(handler)


Setup via logging dict config
-----------------------------

Here is code::

  # -*- coding: utf8 -*-

  import logging

  logging.config.dictConfig({
      "handlers": {
        "kids": {
            "class": "kids.KidsHandler"
        }
      },
      "loggers": {
          "test": {
              "handlers": [kids]
          }
      }
  })
