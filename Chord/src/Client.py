from Node import Peer
from Chord import Server
import time

#print proxy
#print proxy.successorId
#print "The successor of 15: %s" % str(proxy.find_successor(100))


server = Server(120)
server.start()

while server.get_peer() is None:
    doNothing = 1;

new_peer = server.get_peer()
new_peer.join(155)

time.sleep(5)
new_peer.print_chord()

