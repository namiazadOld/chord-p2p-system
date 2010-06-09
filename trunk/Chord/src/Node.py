'''
Created on Jun 4, 2010

@author: nami
'''
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import xmlrpclib
import threading

class RequestHandler(SimpleXMLRPCRequestHandler):
    def __init__(self, request, client_address, server, client_digest=None):
        SimpleXMLRPCRequestHandler.__init__(self, request, client_address, server)
            
class Peer:
    def __init__(self, id, m = 8): 
        self.id = id
        self.predecessorId = None
        self.successorId = id 
        self.finger = []
        self.next = 0
        self.m = m
    def find_successor(self, id):
        if id > self.id and id < self.successorId :
            return self.successorId
        else :
            successor = xmlrpclib.ServerProxy("http://localhost:" + str(8000 + self.successorId))
            return successor.find_successor(id)
    def join(self, targetId):
        self.predecessorId = None
        target = xmlrpclib.ServerProxy("http://localhost:" + str(8000 + targetId))
        self.successorId = target.find_successor(self.id)
    def stabilize(self):
        successor = xmlrpclib.ServerProxy("http://localhost:" + str(8000 + self.successorId))
        x = successor.get_predecessorId()
        if x > self.id and x < self.successorId :
            self.successorId = x
        successor.notify(self.id)
    def notify(self, targetId):
        if self.predecessorId == None or (targetId > self.predecessorId and targetId < self.id) :
            self.predecessorId = targetId
    def set_successor(self, successorId):
        self.successorId = successorId
    def get_successor(self):
        return self.successorId
    def get_predecessorId(self):
        return self.predecessorId
    def print_node(self):
        print "NodeID = " + str(self.id) + " SuccessorID = " + str(self.successorId) + " Predecessor = " + str(self.predecessorId)
    def print_chord(self, sourceId = None):
        if (sourceId == None):
            sourceId = self.id
        self.print_node()
        if (self.successorId != sourceId):
            successor = xmlrpclib.ServerProxy("http://localhost:" + str(8000 + self.successorId))
            successor.print_chord(sourceId)
    def stabilize_all(self, sourceId = None):
        if (sourceId == None):
            sourceId = self.id
        self.stabilize()
        if (self.successorId != sourceId):
            successor = xmlrpclib.ServerProxy("http://localhost:" + str(8000 + self.successorId))
            successor.stabilize_all(sourceId)
    def fix_fingers(self):
        self.next = (self.next % self.m) + 1
        self.finger[next] = self.find_successor(self.id + pow(2,self.next - 1))
    def closest_preceding_finger(self, nodeId):
        counter = self.m
        while counter > 0 :
            if self.finger[counter] > self.id and self.finger[counter] < nodeId :
                return self.finger[counter]
        return self.id
    def find_predecessor(self, nodeId):
        tempId = self.id
        temp = xmlrpclib.ServerProxy("http://localhost:" + str(8000 + tempId))
        while nodeId < tempId or nodeId > temp.get_successor :
            tempId = temp.closest_preceding_finger(nodeId)
            temp = xmlrpclib.ServerProxy("http://localhost:" + str(8000 + tempId))
        return tempId
                 
        
       
            