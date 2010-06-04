'''
Created on Jun 4, 2010

@author: nami
'''
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    def __init__ (self, id):
        self.rpc_paths = ('/' + str(id))

class Peer:
    successorId = -1
    def find_successor(self, id):
        return id
        