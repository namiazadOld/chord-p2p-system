'''
Created on Jun 4, 2010

@author: nami
'''
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    def __init__(self, request, client_address, server, client_digest=None):
        SimpleXMLRPCRequestHandler.__init__(self, request, client_address, server)
    def set_id(self, nodeId):
        self.rpc_paths = ('/' + str(nodeId),)
            
class Peer:
    successorId = -1
    def __init__(self, id):
        self.id = id
    def find_successor(self, id):
        return id
        