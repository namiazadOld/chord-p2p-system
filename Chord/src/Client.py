from Node import Peer

#print proxy
#print proxy.successorId
#print "The successor of 15: %s" % str(proxy.find_successor(100))

new_peer = Peer(120)
new_peer.join(134)
new_peer.stabilize()
new_peer.print_chord()

