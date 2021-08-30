import time
import zmq

print("going to receive...", flush=True)
time.sleep(5)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print("bind...", flush=True)

while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message, flush=True)

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send(b"World")


