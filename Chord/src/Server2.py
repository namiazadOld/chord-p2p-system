'''
Created on May 28, 2010

@author: nami
'''

import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer

class Node:
    id = 10;
    successor_id = 20;
    def find_successor(self, id):
        if id > self.id and id < self.successor_id :
            return self.successor_id
        else :
            successor = xmlrpclib.ServerProxy("http://localhost:8000/")
            
def is_even(n):
    return n%2 == 0

server = SimpleXMLRPCServer(("localhost", 8000))
print "Server 1 is listening on port 8000..."
server.register_introspection_functions()
server.register_function(is_even, "is_even")
server.register_instance(Node())
server.serve_forever()

def main():
    print "hello"
        
if __name__ == '__main__':
    main()
    