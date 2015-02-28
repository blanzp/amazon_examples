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

q = conn.get_queue('halo_man_position')
print 'queue is', q

msg = Message()
msg.set_body('i moved to new location')

msg.message_attributes = {
    "latitude": {
        "data_type": "Number",
        "string_value": "21212"
    },
    "longitude": {
        "data_type": "Number",
        "string_value": "2323"
    }
}

msg_sent = q.write(msg)

# now read the message
msg_received = q.read()
print msg_received.get_body()

conn.close()
