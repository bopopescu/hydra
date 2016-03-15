__author__ = 'AbdullahS, sushil'

from pprint import pprint, pformat   # NOQA
import zmq
import logging
import json
import sys
from hydra.lib import util

l = util.createlogger('HDaemon', logging.INFO)
# l.setLevel(logging.DEBUG)


class HAnalyser(object):
    def __init__(self, server_ip, server_port):
        l.debug("Hydra Analyser initiated...")
        self.server_ip = server_ip
        self.port = server_port
        self.data = {}  # This is where all received data will be stored

        self.context = zmq.Context()
        l.debug("Connecting to server at [%s:%s]", self.server_ip, self.port)
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://%s:%s" % (self.server_ip, self.port))
        l.debug("Conneced...")

    def do_req_resp(self, msg_send, msg_args=None):
        smsg = [msg_send, msg_args]
        l.debug("Sending message %s" % pformat(smsg))
        self.socket.send(json.dumps(smsg))
        l.debug("Waiting for server to respond...")
        rep = self.socket.recv()
        l.debug("Got response %s" % pformat(rep))
        r = json.loads(rep)
        return (r[0], r[1])

    def do_ping(self):
        (status, response) = self.do_req_resp('ping')
        return (status == 'ok') and (response == 'pong')

    def stop(self):
        self.socket.close()


if __name__ == '__main__':
    # Standalone implementation goes here if required
    sys.exit(0)