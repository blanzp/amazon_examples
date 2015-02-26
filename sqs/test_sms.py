__author__ = 'blanzp'

from boto.sqs import connect_to_region
from boto.sqs.queue import Queue
from boto.sqs.connection import SQSConnection
from boto.sqs.message import Message
import unittest
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("/home/blanzp/amazon.cfg")

# must wait > 60 sec between test runs

class SMSMessageTest(unittest.TestCase):
    TEST_QUEUE = 'create_test'

    @classmethod
    def setUpClass(sms):
        print "Creating connection"
        sms.conn = connect_to_region(
            config.get('amazon', 'region'),
            aws_access_key_id=config.get('amazon', 'AWSAccessKeyId'),
            aws_secret_access_key=config.get('amazon', 'AWSSecretKey'))

    def test_connection(self):
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

    def test_send_receive_message(self):
        q = self.conn.create_queue('message_test')
        msg_created = Message()
        msg_created.set_body('hello world')
        msg_sent = q.write(msg_created)
        self.assertEquals(msg_created, msg_sent)
        read_msg = q.read()
        self.assertIsNotNone(read_msg)
        self.assertEquals(msg_created.get_body(), read_msg.get_body())

    @classmethod
    def tearDownClass(sms):
        print "Removing queues and closing connection"
        queues_left = sms.conn.get_all_queues()
        for queue in queues_left:
            print "removing queue", queue.name, queue.url
            sms.conn.delete_queue(queue, force_deletion=True)
        sms.conn.close()
