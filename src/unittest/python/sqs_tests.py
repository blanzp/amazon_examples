__author__ = 'blanzp'

from unittest import TestCase
from boto.sqs import connect_to_region
from boto.sqs.queue import Queue
from boto.sqs.connection import SQSConnection
from boto.sqs.message import Message
import mock

class TestSQS(TestCase):
    TEST_QUEUE = 'foo'

    def setUp(self):
        self.conn = connect_to_region(
            'us-west-2',
            aws_access_key_id='blah',
            aws_secret_access_key='blah')
        self.assertIsInstance(self.conn, SQSConnection)

    @mock.patch("boto.sqs.connection.SQSConnection.get_object")
    def test_create_queue(self, mock_connection):
        return_queue = Queue
        return_queue.name = 'foo'
        mock_connection.return_value = return_queue
        q = self.conn.create_queue(self.TEST_QUEUE)
        self.assertEquals(q.name, self.TEST_QUEUE)