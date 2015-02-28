__author__ = 'blanzp'

from boto.sqs import connect_to_region
from boto.sqs.message import Message
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("/home/blanzp/amazon.cfg")

conn = connect_to_region(
    config.get('amazon', 'region'),
    aws_access_key_id=config.get('amazon', 'AWSAccessKeyId'),
    aws_secret_access_key=config.get('amazon', 'AWSSecretKey'))

q = conn.create_queue('mack')
print 'queue is', q
msg = Message()
msg.set_body('hello there pops')
msg_sent = q.write(msg)
#msg_received = q.read()
#print msg_received.get_body()

conn.close()
