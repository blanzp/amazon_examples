__author__ = 'blanzp'

import boto


class Connection(boto.sms.connection):
    DEFAULT_DOMAIN = 'default_domain'
    DEFAULT_SCOPE = 'local'

    def __init__(self):
        super(Connection, self).__init__()

    def create_queue(self, queue_name, domain=DEFAULT_DOMAIN, scope=DEFAULT_SCOPE, visibility_timeout=None):
        queue_name = "{}${}${}".format(domain,scope,queue_name)
        return super(Connection, self).create_queue(queue_name, visibility_timeout=None)

    def get_queue(self, queue_name, domain=DEFAULT_DOMAIN, scope=DEFAULT_SCOPE, visibility_timeout=None):
        queue_name = "{}${}${}".format(domain,scope,queue_name)
        return super(Connection, self).get_queue(queue_name, visibility_timeout=None)
