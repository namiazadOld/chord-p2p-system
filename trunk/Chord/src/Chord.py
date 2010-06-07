'''
Created on Jun 4, 2010

@author: nami
'''

from Node import RequestHandler
from Node import Peer
from random import randint
from threading import Thread
from SimpleXMLRPCServer import SimpleXMLRPCServer
import xmlrpclib

class Server(Thread):
    def __init__(self, nodeId): 
        Thread.__init__(self)
        self.nodeId = nodeId
        self.new_peer = None
    def get_peer(self):
        return self.new_peer
    def run(self):
        peer = SimpleXMLRPCServer(("localhost", 8000 + self.nodeId), requestHandler = RequestHandler, allow_none = True)
        print "Peer " + str(self.nodeId) + " is listening on port " + str(8000 + self.nodeId) + "..."
        peer.register_introspection_functions()
        self.new_peer = Peer(self.nodeId)
        peer.register_instance(self.new_peer)
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
        server = Server(nodeIdList[count])
        server.start()
        count = count + 1
        
    #Stabilizing the new created ring (setting the predecessors)
    count = 0
    while count < n:
        currentId = nodeIdList[count]
        successorId = nodeIdList[(count + 1) % n]
        current = xmlrpclib.ServerProxy("http://localhost:" + str(8000 + currentId))
        current.set_successor(successorId)
        successor = xmlrpclib.ServerProxy("http://localhost:" + str(8000 + successorId))
        successor.notify(currentId)     #set predecessor of successor
        count = count + 1
    
    start_node = xmlrpclib.ServerProxy("http://localhost:" + str(8000 + nodeIdList[0]))
    start_node.print_chord()
    print 'Finish'
    
if __name__ == '__main__':
    Chord(8, 4)