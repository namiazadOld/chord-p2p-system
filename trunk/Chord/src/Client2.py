import xmlrpclib
start_node = xmlrpclib.ServerProxy("http://localhost:" + str(8120))
start_node.print_chord()

f  = open('d:\pp.txt', 'w')
