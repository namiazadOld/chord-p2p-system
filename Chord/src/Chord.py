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
    def __init__(self, nodeId, successorId):
        Thread.__init__(self)
        self.nodeId = nodeId
        self.nextId = successorId
    def run(self):
        peer = SimpleXMLRPCServer(("localhost", 8000 + self.nodeId), requestHandler = RequestHandler)
        print "Peer " + str(self.nodeId) + " is listening on port " + str(8000 + self.nodeId) + "..."
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
    
    nodeIdList.sort()
    count = 0;
    while count < n:
        server = Server(nodeIdList[count], nodeIdList[(count + 1) % n])
        server.start()
        count = count + 1

if __name__ == '__main__':
    Chord(8, 60)