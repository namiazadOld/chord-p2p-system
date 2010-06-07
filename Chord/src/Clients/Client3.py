import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://localhost:8000/10")
print proxy
print "The successor of 15: %s" % str(proxy.find_successor(186))
