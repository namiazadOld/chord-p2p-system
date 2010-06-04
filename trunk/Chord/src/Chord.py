'''
Created on Jun 4, 2010

@author: nami
'''

from Node import RequestHandler
from Node import Peer
from random import randint
from threading import Thread
from SimpleXMLRPCServer import SimpleXMLRPCServer


class Server(Thread):
    def __init__(self, nodeId):
        Thread.__init__(self)
        self.nodeId = nodeId
    def run(self):
        peer = SimpleXMLRPCServer(("localhost", 8000), requestHandler = RequestHandler)
        print "Peer " + str(self.nodeId) + " is listening on port 8000..."
        peer.register_introspection_functions()
        peer.register_instance(Peer(self.nodeId))
        peer.serve_forever()
        

def Chord(m, n):
    count = 0;
    M = pow(2, m)
    nodeIdList=[]
    while count < n:
        nodeId = randint(1, M)
        if nodeId in nodeIdList:
            continue
        nodeIdList.append(nodeId)
        count = count + 1
        server = Server(nodeId)
        server.start()
        

if __name__ == '__main__':
    Chord(8, 1)