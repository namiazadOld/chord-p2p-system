'''
Created on Jun 4, 2010

@author: nami
'''
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from SimpleXMLRPCServer import SimpleXMLRPCServer

id = 10

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/10',)
    
class Peer:
    successorId = -1
    def find_successor(self, id):
        return id

peer = SimpleXMLRPCServer(("localhost", 8000), requestHandler = RequestHandler)
print "Peer " + str(id) + " is listening on port 8000..."
peer.register_introspection_functions()
peer.register_instance(Peer())
peer.serve_forever()
