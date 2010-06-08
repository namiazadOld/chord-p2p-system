import xmlrpclib

start_node = xmlrpclib.ServerProxy("http://localhost:8155" )
start_node.print_chord()
print 'Finish'
