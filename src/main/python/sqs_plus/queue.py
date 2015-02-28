__author__ = 'blanzp'

import boto


class Queue(boto.sqs.queue.Queue):

    def _name(self):
        queue_name = super(Queue, self)._name()
        [self.domain, self.scope, self.name] = queue_name.split('$')
        return self.name
    name = property(_name)
