# -*- coding: utf -*-
"""
    kids.log_handler
    ~~~~~~~~~~~~~~~~

    Kids Log Handler.
"""

import logging
import redis
import socket
import time


class KidsFormatter(logging.Formatter):

    """Kids Log Formatter.
    """

    def __init__(self):
        super(KidsFormatter, self).__init__()
        self._hostname = socket.gethostname()
        self._fmt = '[%(levelname).1s %(asctime)s %(module)s:%(lineno)d %(host)s:%(process)d] %(message)s'  # noqa

    def format(self, record):
        """Format record.

        :param logging.LogRecord record: LogRecord instance
        """
        # Format asctime.
        tmp_date = self.converter(record.created)
        record.asctime = time.strftime("%y%m%d %H:%M:%S", tmp_date)
        record.host = self._hostname
        return super(KidsFormatter, self).format(record)


class KidsHandler(logging.Handler):

    """Kids Log Handler.
    """

    def __init__(self, port=3388, host="localhost", topic=None):
        """Initialize.

        :param int port: Kids server port
        :param str host: Kids server hostname
        :param str topic: Kids topic, default is kids
        """
        super(KidsHandler, self).__init__()
        self.kids = redis.StrictRedis(host=host,
                                      port=port)
        self.formatter = KidsFormatter()
        self.topic = topic

    def emit(self, record):
        """Override default emit method to
        send record to kids server.

        :param logging.LogRecord record: LogRecord instance
        """
        # Set topic.
        if not self.topic:
            topic = record.name  # Using logger name as topic.
        else:
            topic = self.topic

        record.message = record.getMessage()
        raw_record = self.formatter.format(record)
        try:
            self.kids.publish(topic, raw_record)
        except (redis.ConnectionError, redis.TimeoutError, SystemExit):
            # Handle publish message error, and log to stderr.
            self.handleError(record)
        except Exception:
            pass
