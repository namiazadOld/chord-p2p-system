
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/10',)
    
class Node:
    id = 10;
    successor = 20;
    def find_successor(self, id):
        if id > self.id and id < self.successor :
            return self.successor

def is_even(n):
    return n%2 == 0

server = SimpleXMLRPCServer(("localhost", 8000), requestHandler=RequestHandler)
print "Server 1 is listening on port 8000..."
server.register_introspection_functions()
server.register_function(is_even, "is_even")
server.register_instance(Node())
server.serve_forever()

def main():
    print "hello"
        
if __name__ == '__main__':
    main()
    