__author__ = 'blanzp'

from boto.sqs import connect_to_region
from boto.sqs.queue import Queue
from boto.sqs.connection import SQSConnection
from boto.sqs.message import Message
import unittest
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("/home/blanzp/amazon.cfg")


class SMSMessageTest(unittest.TestCase):
    TEST_QUEUE = 'myqueue'

    def setUp(self):
        self.conn = connect_to_region(
            config.get('amazon', 'region'),
            aws_access_key_id=config.get('amazon', 'AWSAccessKeyId'),
            aws_secret_access_key=config.get('amazon', 'AWSSecretKey'))
        self.assertIsInstance(self.conn, SQSConnection)

    def test_create_queue(self):
        q = self.conn.create_queue(self.TEST_QUEUE)
        self.assertIsInstance(q, Queue)
        self.assertEquals(q.name, self.TEST_QUEUE)

    def test_delete_queue(self):
        q = self.conn.create_queue('delete_test')
        self.conn.delete_queue(q, force_deletion=True)
        queue_delete = self.conn.get_queue('delete_test')
        self.assertIsNone(queue_delete)